
### 使用pycharm新建Django项目

## 1、pycharm下载安装
[pycharm付费版下载地址](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac&code=PCC)
[pycharm免费版](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac)
这里建议下载付费版软件，然后找一下破解方式，找不到破解方式的可以私信我

## 2、新建Django项目
打开pycharm，按照下图指示
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-1.png)
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-2.png)

## 3、model的创建
1.新建app，导航栏中点击Tools，调起“manage.py”，如下图
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-3.png)
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-4.png)
2.在TestModel下的models.py中写入model各个类的属性，
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-5.png)
```base
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#引用django.db中的models
from django.db import models

class Test(models.Model):
name = models.CharField(max_length=20)

class Contact(models.Model):
name = models.CharField(max_length=200)
age = models.IntegerField(default=0)
email = models.EmailField()
def __str__(self):
return self.name

class Tag(models.Model):
contact = models.ForeignKey(Contact)
name = models.CharField(max_length=50)
def __str__(self):
return self.name
```
更多模型字段可参考[模型字段](http://python.usyiyi.cn/translate/django_182/ref/models/fields.html)

## 4、setting的配置
在项目中找到“settings.py“文件（路径：～／projectName/projectName/settings.py）
1.配置mysql连接信息
```base
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',# 或者使用 mysql.connector.django
        'NAME': 'hello',#数据库名称
        'USER': 'root',#用户名
        'PASSWORD': '11111111',
        'HOST': 'localhost',#主机
        'PORT': '3306',#端口
    }
}
```
2.在INSTALLED_APPS中添加刚刚注册的app
```base
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',
]
```
3.安装数据库驱动
需要使用pip在虚拟环境（解释器环境）中安装支持库
```base
pip install mysqlclient
```

## 5、makemigrations与migrate的使用
导航栏中点击Tools，调起“manage.py”
makemigrations：相当于在该app下建立migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py， 但是这个改动还没有作用到数据库文件
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-6.png)
你可以手动打开这个文件，看看里面是什么。当makemigrations之后产生了0001_initial.py 文件，你可以查看下该migrations会对应于什么样子的SQL命令，使用如下命令
```base
sqlmigrate TestModel 0001
```
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-10.png)
migrate：将该改动作用到数据库文件，比如产生table之类
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-7.png)
自动生成的
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-8.png)
mysql数据库中生成自动生成的
![image](https://raw.githubusercontent.com/ly92/images/master/django/2-9.png)

