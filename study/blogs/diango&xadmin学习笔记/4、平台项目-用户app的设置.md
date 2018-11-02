
### Django实战项目-自定义用户app以及其他app的设计（1）

## 1、自定义用户表
Django中自带了用户表，但是有时候我们需要的用户属性与自带表有差别，这时我们可以自定义用户表的字段来达到目的
系统默认的用户表在“django.contrib.auth.models”中的“AbstractUser”可以自行打开看一下都有什么字段，下面我们需要继承这个model新建一个用户model，起名为“UserProfile”
```base
from django.contrib.auth.models import AbstractUser#首先导入AbstractUser

class UserProfile(AbstractUser):#继承，下面是新增字段
nick_name = models.CharField(max_length=50, verbose_name='昵称', default="")
birday = models.DateTimeField(verbose_name="生日", null=True, blank=True)
gender = models.CharField(max_length=10, choices=(("male","男"),("female","女")),default="female")
address = models.CharField(max_length=100, default="")
mobile = models.CharField(max_length=11, null=True, blank=True)
image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

class Meta:#model的描述信息
verbose_name = "用户信息"
verbose_name_plural = verbose_name

def __str__(self):
return self.username
```
## 2、setting的设置
上面自定义了UserProfile后需要在setting中告诉系统谁是用户表，只需加下面一行
```base
AUTH_USER_MODEL = "users.UserProfile"
```

## 3、其他app的设计
项目中表的结构示意图：
![image](https://raw.githubusercontent.com/ly92/images/master/django/4-1.png)
打开manage.py终端使用startapp name新建上图所示4个app，并在app下的models.py中建立相应的类和属性
![image](https://raw.githubusercontent.com/ly92/images/master/django/4-2.png)
在项目目录下新建一个文件夹命名“apps”用来存放上面的四个app，直接选中拖拽到apps目录下
不必勾选上面的选项
![image](https://raw.githubusercontent.com/ly92/images/master/django/4-3.png)
然后将apps设置为源文件路径
![image](https://raw.githubusercontent.com/ly92/images/master/django/4-4.png)

## 4、setting的设置
1.首先要告知系统apps的路径
```base
import sys   #引入sys
在   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))下面添加
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
```
添加app
```base
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'users',
'courses',
'organization',
'operation',
]
```
## 5、表之间的关系表示（外键）
在operation中新建CourseComments类的时候有user属性和course属性
```base
#首先导入文件
from users.models import UserProfile
from courses.models import Course

class CourseComments(models.Model):
user = models.ForeignKey(UserProfile, verbose_name="用户")#外键
course = models.ForeignKey(Course, verbose_name="课程")#外键
comments = models.CharField(max_length=200, verbose_name="评论内容")
add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

class Meta:
verbose_name = "课程评论"
verbose_name_plural = verbose_name
```

