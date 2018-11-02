#centos7.4 python3.6.4 django2 uwsgi mysql 

1.安装python3，./configure   make && make install
2.Django
3.uwsgi
4.nginx
5.mysql-navicat连接

python断断续续的学习了一段时间，一直是在Mac上面跑跑，最近阿里云打折便买了一个便宜的服务器来玩，在阿里云网站的控制台中找到自己购买的实例，打开远程连接进入终端输入账号密码就可以开始配置环境了
##1、安装Python3.6.4
目前centos中默认的python是2.7版本，现在需要升级到3.6.4版本，首先下载，解压后配置并安装
```
下载
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

解压
tar xf Python-3.6.4.tgz

进入到解压得到的文件夹中
cd Python-3.6.4

依次键入或者复制命令输入
./configure --prefix=/opt/python3 

make && make install 

```
安装完毕后查看python版本
```
默认python版本 --> 2.7
python --version

python3版本 --> 3.6.4
python3 --version
```
如果版本为3.6.4则说明安装成功，有强迫症的可以把python3.6.4的压缩包和解压包都删除

##2、安装Django
Django已经进入2.0版本了，如果直接用“pip install django”会安装失败，因为pip默认的是python2.7，Django2不支持python2，下面命令可以直接安装Django版本
```
pip3 install django
```
进入到“/home”路径中，使用下面命令测试是否安装Django成功，同时也是在新建项目"mysite"
```
django-admin.py startproject mysite
```
```
cd mysite/mysite
```
编辑项目settings.py文件,在ALLOWED_HOSTS中添加自己的公网IP
```
vim settings.py
```

执行项目
```
cd ../
python3 manage.py runserver 0.0.0.0:80

退出
control + C
```
在浏览器中输入“http://公网ip”一般情况下会展示Django启动成功的画面，如果展示的是服务器未响应，在ip地址无误的情况下首先查看是否为自己的无服务实例设置安全组端口范围为“80/80”，如果还是未响应那么查看一下设置防火墙

##3、安装uwsgi
使用pip安装
```
pip3 install uwsgi
```
安装结束后回到根目录下,创建test.py文件,并编辑
```
cd （或者 cd ~）

touch test.py

vi test.py
```
内容为下，最好是使用sublime创建一个test.py然后通过filezilla传到服务器根目录下，防止因为格式导致的问题
```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return b"Hello World"
```
在终端运行下面命令
```
uwsgi --http :80 --wsgi-file test.py
```
然后在浏览器中输入“http://公网ip”，如果看到“Hello World”则表示成功

##4、安装Nginx
返回到根目录，下载，解压，配置，安装
```
wget http://nginx.org/download/nginx-1.13.7.tar.gz

tar xf nginx-1.13.7.tar.gz

cd nginx-1.13.7

./configure --prefix=/usr/local/nginx-1.13.7 --with-http_stub_status_module --with-http_gzip_static_module

make && make install
```

80端口比较容易被别的程序占用，可以改“nginx.conf”里面的监听端口，如果不知道某些文件的路径可以通过下面命令查找
```
find / -name nginx.conf
```
会列出所有“nginx.conf”所存在的位置，修改“/usr/local/nginx-1.13.7/conf/nginx.conf”
启动nginx
```
/usr/local/nginx-1.13.7/sbin/nginx
```
然后在浏览器中输入“http://公网ip”，如果看到nginx的欢迎页面则安装成功

##5、配置uwsgi启动项目
首先项目“mysite”中创建“mysite_uwsgi.ini”文件
```
cd /home/mysite

touch mysite_uwsgi.ini

```
复制下面代码入“mysite_uwsgi.ini”
```
# mysite_uwsgi.ini file
[uwsgi]

# Django-related settings

http = :8008

# the base directory (full path)
chdir           = /home/mysite

# Django s wsgi file
module          = mysite.wsgi

# process-related settings
# master
master          = true

# maximum number of worker processes
processes       = 4

# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true

```
修改nginx.conf文件

```
include uwsgi_params; 
uwsgi_pass 127.0.0.1:8008;（端口要与ini中的端口一致）
```

执行命令后能够查看网页并且按“control + C”后依然可以访问说明成功
```
uwsgi --ini /home/mysite/mysite_uwsgi.ini & /usr/local/nginx-1.13.7/sbin/nginx
```

##6、安装Mysql
回到根目录
下载，安装
```
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm

rpm -ivh mysql-community-release-el7-5.noarch.rpm

yum install mysql-community-server
```
初次安装无需密码即可登录
```
mysql -u root 
```
设置密码
```
mysql> set password for 'root'@'localhost' =password('password');
```
在jianshu的settings.py中配置数据库连接
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jianshu',
        'USER': 'root',
        'PASSWORD': '11111111',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```












