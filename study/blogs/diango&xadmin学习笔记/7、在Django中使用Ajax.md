### Django实战项目-在Django中使用Ajax (4）

##1.ModelForm
ModelForm与之前见到的Form效果一样，用着跟方便，使用下面方式导入
```base
from django import forms
```
对于下面这个model使用ModelForm与Form的两种方式
```base
class UserAsk(models.Model):
	name = models.CharField(max_length=20, verbose_name="姓名")
	mobile = models.CharField(max_length=11, verbose_name="手机号")
	course_name = models.CharField(max_length=50, verbose_name="课程名称")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = "用户咨询"
		verbose_name_plural = verbose_name
```
两种方式中如果model的属性比较多用第二种会麻烦很多
```base
class UserAskForms(forms.ModelForm):
    mobile = forms.CharField(required=True,max_length=11, min_length=11)
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
```
```base
class UserAskForms(Form):
	name = forms.CharField(required=True)
	mobile = forms.CharField(required=True, max_length=11, min_length=11)
	course_name = forms.CharField(required=True)
```
使用方式两者无异
```base
user_ask_form = UserAskForms(request.POST)
if user_ask_form.is_valid():
````

##2.Ajax的使用
##2.1
html中的代码
```base
 <div class="right companyright">
                <div class="head">我要学习</div>
                <form class="rightform" id="jsStayForm" method="post">
                    <div>
                        <img src="{% static 'images/rightform1.png' %}"/>
                        <input type="text" name="name" id="companyName" placeholder="名字" maxlength="25"/>
                    </div>
                    <div>
                        <img src="{% static 'images/rightform2.png' %}"/>
                        <input type="text" name="mobile" id="companyMobile" placeholder="联系电话"/>
                    </div>
                    <div>
                        <img src="{% static 'images/rightform3.png' %}"/>
                        <input type="text" name="course_name" id="companyAddress" placeholder="课程名" maxlength="50"/>
                    </div>
                    <p class="error company-tips" id="jsCompanyTips"></p>
                    <input class="btn" type="button" id="jsStayBtn" value="立即咨询 >"/>
                    <input type='hidden' name='csrfmiddlewaretoken' value='5I2SlleZJOMUX9QbwYLUIAOshdrdpRcy'/>
                    {% csrf_token %}
                </form>
            </div>
```

view的代码
```base
class AddUserAskView(View):
    """
       用户添加咨询
    """
    def post(self, request):
        user_ask_form = UserAskForms(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            return HttpResponse('{"status" : "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status" : "fail", "msg" : "添加出错"}', content_type='application/json')

```

script代码
```base
<script>
        $.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});
        $(function () {
            $('#jsStayBtn').on('click', function () {
                $.ajax({
                    cache: false,
                    type: "POST",
                    url: "{% url 'org:user_ask' %}",
                    data: $('#jsStayForm').serialize(),
                    async: true,
                    success: function (data) {
                        if (data.status == 'success') {
                            $('#jsStayForm')[0].reset();
                            alert("提交成功")
                        } else if (data.status == 'fail') {
                            $('#jsCompanyTips').html(data.msg)
                        }
                    },
                });
            });
        })
    </script>
```
##2.2遇到的问题
1.403 csrf
在html中添加了“{% csrf_token %}”但是依然会提示403错误，看到别人说是由于setting.py中的“MIDDLEWARE”添加了“'django.middleware.csrf.CsrfViewMiddleware',”这个要加上，为了数据安全
在script中需要加上才能避免403错误
```base
$.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});
```

2.无法获取form里传的数据
我在开发过程中遇到了无法得到form里面传的数据，取数据是用“$('#jsStayForm').serialize()”，这样没有必要对每一个参数都写一遍


