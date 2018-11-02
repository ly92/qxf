
#Python 简单爬虫入门
#1.目标
从简书的[作者推荐](http://www.jianshu.com/recommendations/users?utm_source=desktop&utm_medium=index-users)中获取所有的头像，保存到本地，名称为作者的名字，[GitHub源码](https://github.com/ly92/reptile)
#2.三方库以及工具准备
2.1~2.4是需要使用的三方库，使用pip安装在 [虚拟环境](http://www.jianshu.com/p/5f46412c6f12)中
##2.1 requests
[快速入门](http://docs.python-requests.org/zh_CN/latest/)，请求数据
```base
pip install requests
```
##2.2 selenium
[快速入门](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html)，自动化操作
```base
pip install selenium
```
##2.3 lxml
[快速入门](http://lxml.de/index.html)
```base
pip install lxml
```
##2.4 beautifulsoup4
[快速入门](http://beautifulsoup.readthedocs.io/zh_CN/latest/#id1)，获取html，xml的数据
```base
pip install beautifulsoup4
```
##2.5 phantomjs
[快速入门](http://phantomjs.org/documentation/),无界面的浏览器
```base
brew install phantomjs
```
#3.selenium模拟搜索
在[简书](http://www.jianshu.com)首页搜索“python”，并输出搜索内容
这里使用Mac的Safari，首先需要在Safari的偏好设置里面选中“在菜单栏中显示‘开发’菜单”，然后允许远程自动化，如果运行失败尝试退出Safari后重试。自己尝试一下，期间不要点击Safari，不是Mac的同学可以使用其他浏览器
![image](https://raw.githubusercontent.com/ly92/images/master/reptile/reptile1.png)
![image](https://raw.githubusercontent.com/ly92/images/master/reptile/reptile2.png)
```base
import time
from selenium import webdriver

//自动用简书搜索Python
driver = webdriver.Safari()//实例化Safari浏览器
driver.get("http://www.jianshu.com")//加载网页
print(driver.title)//输出网页title
elem = driver.find_element_by_name("q")//获取搜索框，搜索框的name为“q”
elem.clear()//清空搜索框
elem.send_keys("python")//输入搜索关键字
elem.send_keys(Keys.RETURN)//点击搜索
time.sleep(3)//防止网速不好时搜索不到内容
print(driver.page_source)//输出搜索内容
assert "No results found." not in driver.page_source
driver.close()//一定要关闭，否则不可进行第二次
```
#4.开始爬取头像
##4.1、引入头文件
```base
import requests
from bs4 import BeautifulSoup
import lxml
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```
##4.2、浏览器驱动
```base
def request(self,url):
    driver = webdriver.PhantomJS()//使用无页面的PhantomJS
    driver.get(url)
    self.click_more(driver,5)//模拟点击5次
    return driver.page_source
```
##4.3、点击“加载更多”按钮
```base
def click_more(self,driver,times):
    for i in range(times):
        print("开始执行第", str(i + 1),"次点击操作")
        #复合类的名称不允许，所以使用下面的方式
        # elem = driver.find_element_by_class_name("btn btn-danger load-more-btn")
        elem = driver.find_element_by_class_name("load-more-btn")
        elem.click()
        time.sleep(5)//每次点击后给一定的加载时间
```
##4.4、创建路径
如果路径存在的话下载图片时需要去重，如果路径是新建的则不需要去重，这里使用作者的名字当作去重的标准
```base
def mkdir(self, path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print('创建名字叫做', path, '的文件夹')
        os.makedirs(path)
        print('创建成功！')
        return True
    else:
        print(path, '文件夹已经存在了，不再创建')
        return False
```
##4.5、处理爬取的数据，获取图片url和名称
每一个推荐作者的数据是一个div
```base
<div class="col-xs-8">
    <div class="wrap">
        <a target="_blank" href="/users/5SqsuF">
        <img class="avatar" src="//upload.jianshu.io/users/upload_avatars/6287/06c537002583.png?imageMogr2/auto-orient/strip|imageView2/1/w/180/h/180" alt="180">
        <h4 class="name">
            刘淼

        </h4>
        <p class="description">来，走一圈关注：
        http://www.j...</p>
        </a>
        <a class="btn btn-success follow"><i class="iconfont ic-follow"></i><span>关注</span></a>

        <hr>
        <div class="meta">最近更新</div>
            <div class="recent-update">
                <a class="new" target="_blank" href="/p/5cc6e5ebb742">开车记</a>
                <a class="new" target="_blank" href="/p/828f8c5f82ea">关于时间与金钱的十条感悟</a>
                <a class="new" target="_blank" href="/p/615e75439598">干一票更大的</a>
            </div>
        </div>
</div>
```
```base
def getImgUrlAndName(self, item):
    img = BeautifulSoup(str(item), 'lxml').find('img',class_='avatar',alt='180')
    sufPos = img['src'].rstrip().index('imageMogr2') - 1
    img_url = 'http:' + img['src'][:sufPos]
    suffixPos = img_url.rindex('.')
    suffix = img_url[suffixPos:]
    if suffix.__len__() > 5:
        suffix = '.png'//针对个别不是以图片格式后缀结尾的
    nameStr = BeautifulSoup(str(item), 'lxml').find('h4',class_='name')
    name = nameStr.text.strip() + suffix

    return img_url,name
```

##4.6、处理没一个url和名称
```base
def get_pic(self):
    print('开始网页get请求')
    r = self.request(self.web_url)
    print('开始获取所有item')
    all_item = BeautifulSoup(r, 'lxml').find_all('div',class_='col-xs-8')
    print('开始创建文件夹')
    is_new_folder =  self.mkdir(self.folder_path)//是否存在路径
    print('开始切换文件夹')
    os.chdir(self.folder_path)
    for item in all_item:
    img_url, name = self.getImgUrlAndName(item)
    if is_new_folder:
        self.save_img(img_url, name)
    else:
        all_files = os.listdir(self.folder_path)//获取路径下所有文件，不包含子文件
        if name not in all_files:
        self.save_img(img_url, name)
```
##4.7、保存图片
```base
def save_img(self, url, name):
    print('开始保存图片...%s'%name)
    img = requests.get(url)//获取图片
    time.sleep(5)
    print('开始保存文件')
    f = open(name, 'ab')
    f.write(img.content)
    print(name, '文件保存成功！')
    f.close()
```
##4.8、使用
将以上方法写在BeautifulPicture类中，执行下面代码就可以获取到144个用户的头像和名称，有几个美女作者用的自己的头像哦
```base
beauty = BeautifulPicture()
beauty.get_pic()
```

