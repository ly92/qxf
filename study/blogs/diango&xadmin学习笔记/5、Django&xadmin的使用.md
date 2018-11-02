### Django实战项目-项目中使用xadmin管理（2）

## 1、xadmin下载
在GitHub上面搜索“xadmin”或者点击[xadmin](https://github.com/sshwsfc/xadmin)将代码下载到本地，使用pip安装的xadmin不支持Django1.11，在项目中新建extra_apps文件夹存放引用的别人的三方库，将下载的xadmin文件中的xadmin拷贝到extra_apps中，并将extra_apps mark为源文件路径。
运行时会提示未安装支持库，需要使用pip在虚拟环境（解释器环境）中安装以下支持库,如果提示其他库则按照提示安装即可
```base
pip install django-crispy-forms
pip install django-formtools
pip install future
pip install six
```

## 2、setting配置
添加extra_apps的路径
```base
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))
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
'xadmin',#
'crispy_forms',#
]
```

## 3、app中__init__.py,apps.py,adminx.py修改
adminx.py需要新建不是admin.py,
1.apps.py修改
```base
# -*- coding: utf-8 -*-
from django.apps import AppConfig


class UsersConfig(AppConfig):
name = 'users'
verbose_name = '用户'
```
2.__init__.py修改
```base
default_app_config = "users.apps.UsersConfig"
```
3.新建adminx.py
```base
import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner

下面标记的代码只需写一次即可表示页面的通用配置
###标记开始位置

class BaseSetting(object):
enable_themes = True
use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
site_title = '顶部的名称'
site_footer = '底部的名称'
menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, GlobalSetting)

###标记结束为止

class EmailVerifyRecordAdmin(object):
list_display = ['code', 'email','send_type', 'send_time']
search_fields = ['code', 'email','send_type']
list_filter = ['code', 'email','send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
list_display = ['title', 'image', 'url', 'index', 'add_time']
search_fields = ['title', 'image', 'url', 'index']
list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(Banner, BannerAdmin)
```
orginization的adminx.py
```base
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
list_display = ['name', 'desc', 'add_time']
search_fields = ['name', 'desc']
list_filter = ['name', 'desc', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
list_display = ['name','desc', 'click_nums', 'fav_nums','image', 'address', 'city']
search_fields = ['name','desc', 'click_nums', 'fav_nums','image', 'address', 'city']
list_filter = ['name','desc', 'click_nums', 'fav_nums','image', 'address', 'city']

xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)
```
这里会发现没有写users中的UserProfile类，因为UserProfile是继承的系统的用户类

效果图：
![image](https://raw.githubusercontent.com/ly92/images/master/django/5-1.png)
