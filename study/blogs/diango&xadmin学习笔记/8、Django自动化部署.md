
remote: fatal: Not a git repository: '.'
#Django自动化部署

##概述
在阿里云的centos环境中配置Django的自动部署，平时开发过程中将代码托管在GitHub、gitlab、coding等，我的在coding中，在centos中需要搭建自己的git仓库环境，创建一个空的仓库clone在本地，现在相当于本地有两个项目，一个是自己在coding中的项目，这个是平时开发的，另一个是空文件的项目这个用来记录自己每次发布的概要，这个是提交到自己阿里云的git仓库中的。我现在centos中的home中有“git、NeverGU”两个文件，git是我的仓库，NeverGU是我在coding中的项目。在git中我创建了“NGU.git”文件，这个文件就是我记录每次发布概要的文件，其实不只是那么简单，每次我提交概要到这里的时候NeverGU就会自动更新并且重新发布Django项目，这就是我想要的目的

##具体流程

###1、在centos配置git仓库
####1、检查是否已经安装git
```
git --version
```
####2、如果未安装直接使用yum安装
```
yum install git
```
####3、个人使用时添加一个用户，多人时需要用户组
```
#个人
adduser git

#多人
groupadd git
adduser git -g git
```
####4、修改/etc/passwd文件，修改
```
# 找到这句：
git:x:503:503::/home/git:/bin/bash

# 改为：
git:x:503:503::/home/git:/bin/git-shell
```
####5、创建证书登录
```
mkdir /home/git/.ssh
chmod 700 /home/git/.ssh
touch 700 /home/git/.ssh/authorized_keys
chmod 600 /home/git/.ssh/authorized_keys
```
注意，如果是采用的sudo方式来创建git和相应的文件的，需要设置/home/git/.ssh/的owner为git，否则还是每次要输入密码的。
```
# owner改为git
sudo chown -R git:git /home/git/.ssh/
```
编辑/home/git/.ssh/authorized_keys，把客户端的公钥放进去，公钥在用户主目录里找到.ssh目录“cd ~/.ssh”如果没有则创建
```
ssh-keygen -t rsa -C "youremail@example.com"
```
这时/home目录下就会多一个git文件夹
####6、新建仓库
```
cd /home/git
mkdir NGU.git
cd NGU.git
git init --bare
```
在电脑本地clone“NGU.git”
```
git clone root＠阿里云ip:/home/git/NGU.git
```

###2、post-receive
[关于hooks中的文件的描述参考](https://www.jianshu.com/p/935409ce4c9a)
每次“git push”后得到的通知，会执行post-receive中的脚本，在/home/git/NGU.git/hooks中新增post-receive文件，
```
#!/bin/bash -l
cd /home/NeverGU	#真正的项目目录
unset GIT_DIR		#必要的一步，保证当前git执行的路径
git pull			#啦取最新代码
uwsgi --reload /home/NeverGU/script/uwsgi.pid	#重新部署Django项目
```

就是这么简单，自动部署的方式很多，根据个人习惯，觉得这种不好的可以直接不使用coding等托管代码，直接将自己的代码放在自己的git服务器中，另一种方式也可以使用coding等的git webhook


