
centos7 搭建Laravel开发环境LNMP

##镜像源切换
先把YUM源切换成国内的镜像源
先备份一下原来的源镜像文件
```base
# cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```
下载新的CentOS-Base.repo
```base
#wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```
如果没有安装wget的话可以使用#yum install wget安装完成之后，在执行CentOS-Base.repo的安装
对/etc/yum.repos.d/CentOS-Media.repo源文件配置文件，改为不生效
enable=0
###YUM缓存生成
```base
#yum clean all
#yum makecache
#yum update
```

##安装Nginx

YUM源中没有Nginx，我们需要增加一个nginx的源nginx.repo
```base
# vi /etc/yum.repos.d/nginx.repo
```

```base
源文件的内容
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1
```
查看Nginx是否配置成功
```base
#yum list nginx
```
```base
#yum list |grep nginx
```
安装Nginx官网的最新版本
```base
#yum -y install nginx
```

```base
#nginx #启动Nginx
```

可以使用curl命令查看是否安装成功,如果安装成功的话，就会看到输出一个HTML的一个反馈
```base
#curl 127.0.0.1
```

开机启动设置
```base
#systemctl enable nginx
#systemctl daemon-reload
```

##安装MySql

官网：http://dev.mysql.com/downloads/repo/yum/

查看是否已经启用
```base
#yum repolist all | grep mysql
```
如果没有启用的话，我们可以修改源文件
```base
#/etc/yum.repos.d/mysql-community.repo

[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

```

查看启用版本
```base
#yum repolist enabled | grep mysql
```

```base
#yum -y install mysql-community-server
```
安装完成之后，就可以启动mysql了
```base
#service mysqld start
```
查看MySql的启动状态
```base
#service mysqld status
```

开机启动设置

#systemctl enable mysqld
#systemctl daemon-reload

MySql安装完成之后会在LOG文件(/var/log/mysqld.log)中生成一个root的默认密码

#grep 'temporary password' /var/log/mysqld.log
2017-05-23T14:51:45.705458Z 1 [Note] A temporary password is generated for root@localhost: d&sqr7dcf7P_
登录MySql并修改root密码

#mysql -uroot -p
mysql>ALTER USER 'root'@'localhost' IDENTIFIED BY 'new psd';
扩展阅读：mysql的密码策略

mysql>show variables like '%password%';
+---------------------------------------+--------+
| Variable_name                         | Value  |
+---------------------------------------+--------+
| default_password_lifetime             | 0      |
| disconnect_on_expired_password        | ON     |
| log_builtin_as_identified_by_password | OFF    |
| mysql_native_password_proxy_users     | OFF    |
| old_passwords                         | 0      |
| report_password                       |        |
| sha256_password_proxy_users           | OFF    |
| validate_password_check_user_name     | OFF    |
| validate_password_dictionary_file     |        |
| validate_password_length              | 8      |
| validate_password_mixed_case_count    | 1      |
| validate_password_number_count        | 1      |
| validate_password_policy              | MEDIUM |
| validate_password_special_char_count  | 1      |
+---------------------------------------+--------+
14 rows in set (0.01 sec)
默认的密码策略

validate_password_policy：密码策略，默认为MEDIUM策略 
validate_password_dictionary_file：密码策略文件，策略为STRONG才需要 
validate_password_length：密码最少长度 
validate_password_mixed_case_count：大小写字符长度，至少1个 
validate_password_number_count ：数字至少1个 
validate_password_special_char_count：特殊字符至少1个 
修改密码策略
在/etc/my.cnf文件添加validate_password_policy配置：

# 选择0（LOW），1（MEDIUM），2（STRONG）其中一种，选择2需要提供密码字典文件
validate_password_policy=0
修改默认编码
在/etc/my.cnf配置文件的[mysqld]下添加编码配置：

[mysqld]
character_set_server=utf8
init_connect='SET NAMES utf8'
重启mysql，是修改生效

#systemctl restart mysqld
远程登录用户添加

mysql> GRANT ALL PRIVILEGES ON . TO 'lmc'@'%' IDENTIFIED BY '1qazXsw@' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
查看用户

mysql> select host,user from mysql.user;
+-----------+-----------+
| host      | user      |
+-----------+-----------+
| %         | lmc       |
| localhost | mysql.sys |
| localhost | root      |
+-----------+-----------+
3 rows in set (0.00 sec)
<pre>由于开始没有关闭SELinux，引起mysql连接失败的解决：
http://www.jianshu.com/p/ddd3ce15cb84
</pre>

安装PHP7

#rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
#rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
安装PHP7

#yum install php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-gd.x86_64 php72w-ldap.x86_64 php72w-mbstring.x86_64 php72w-mcrypt.x86_64 php72w-mysql.x86_64 php72w-pdo.x86_64
安装php-fpm

#yum install php72w-fpm php72w-opcache
启动php-fpm

#systemctl start php-fpm
开机启动设置

#systemctl enable php-fpm
#systemctl daemon-reload
修改根目录
修改 /etc/nginx/conf.d/default.conf

项目名为gift，在/home目录下
server {  
        listen  80;    
        server_name www.liyong.work;    
        set $root_path '/home/gift/public';    
        root $root_path;    
        
        index index.php index.html index.htm;    
        
        try_files $uri $uri/ @rewrite;    
        
        location @rewrite {    
            rewrite ^/(.*)$ /index.php?_url=/$1;    
        }    
        
        location ~ \.php {    
        
            fastcgi_pass 127.0.0.1:9000;    
            fastcgi_index /index.php;    
        
            fastcgi_split_path_info       ^(.+\.php)(/.+)$;    
            fastcgi_param PATH_INFO       $fastcgi_path_info;    
            fastcgi_param PATH_TRANSLATED $document_root$fastcgi_path_info;    
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;    
            include                       fastcgi_params;  
        }    
        
        location ~* ^/(css|img|js|flv|swf|download)/(.+)$ {    
            root $root_path;    
        }    
        
        location ~ /\.ht {    
            deny all;    
        }    
    } 
重启Nginx使修改生效
service nginx restart

如果重启失败可能是由于80端口被占用，
netstat -lnp | grep 80

kill -9 进程ID(64384)


git仓库

更改user密码
git仓库：https://www.jianshu.com/p/41f809d06f6a
改user密码：https://blog.csdn.net/qq3965470/article/details/76842181






