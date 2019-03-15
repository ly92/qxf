
进入文件project，并创建一个‘纯净的’python开发环境venv
cd /Users/ly/Desktop/Python/project 
virtualenv --no-site-packages venv
virtualenv -p python3.6 --no-site-packages venv

用source进入该环境，然后安装支持库
source /Users/ly/Desktop/Python/project/venv/bin/activate 

退出当前的venv环境，使用deactivate命令：
deactivate