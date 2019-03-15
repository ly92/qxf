
import requests
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url = 'http://tieba.baidu.com/p/2166231880'
# file = '/Users/ly/Desktop/Python'
# #获取html文件
# def get_html(url):
# 	driver = webdriver.PhantomJS()
# 	driver.get(url)
# 	return driver.page_source
# #新建一个路径 
# def make_dir():
# 	global file
# 	pre_f = '/Users/ly/Desktop/Python/py-test'
# 	t = datetime.now()
# 	file = os.path.join(pre_f, t.strftime('%Y%m%d'))
# 	if os.path.exists(file):
# 		for f in os.listdir(file):
# 			os.remove(os.path.join(file,f))
# 		os.rmdir(file)
# 	os.mkdir(file)
# #开始下载图片
# def get_picture():
# 	make_dir()
# 	source = get_html(url)
# 	imgs = BeautifulSoup(source,'lxml').find_all('img', class_='BDE_Image')
# 	index = 0
# 	for img in imgs:
# 		img_url = img['src'].strip()
# 		print(img_url)
# 		im = requests.get(img_url)
# 		name = os.path.join(file, str(index) + '.jpg')
# 		with open(name,'ab') as f:
# 			f.write(im.content)
# 			f.close()
# 			print('success')
# 		index += 1
# get_picture()


url = r'''
http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1516241968154_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=cat
http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1516241968154_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=cat
'''
file = '/Users/ly/Desktop/Python'
#获取html文件
def get_html(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	return driver.page_source
#新建一个路径 
def make_dir():
	global file
	pre_f = '/Users/ly/Desktop/Python/py-test'
	t = datetime.now()
	file = os.path.join(pre_f, t.strftime('%Y%m%d'))
	if os.path.exists(file):
		for f in os.listdir(file):
			os.remove(os.path.join(file,f))
		os.rmdir(file)
	os.mkdir(file)
#开始下载图片
def get_picture():
	make_dir()
	source = get_html(url)
	imgs = BeautifulSoup(source,'lxml').find_all('li', class_='imgitem')
	index = 0
	for img in imgs:
		img_url = img['data-objurl'].strip()
		im = requests.get(img_url)
		name = os.path.join(file, str(index) + '.jpg')
		with open(name,'ab') as f:
			f.write(im.content)
			f.close()
			print('success')
		index += 1
get_picture()


'''
<li class="imgitem" style="width: 319px; height: 180px; margin-right: 5px; margin-bottom: 5px;" 
data-objurl="http://www.pp3.cn/uploads/201505/2015051901.jpg" data-thumburl="http://img3.imgtn.bdimg.com/it/u=472695846,665540085&amp;
fm=27&amp;gp=0.jpg" data-fromurl="ippr_z2C$qAzdH3FAzdH3Fooo_z&amp;e3Brrn_z&amp;e3BvgAzdH3F15g2AzdH3Fd0c9c_z&amp;e3Bip4s"
 data-fromurlhost="www.pp3.cn" data-ext="jpg" data-saved="0" pn="0" data-pi="0" data-specialtype="0" data-cs="472695846,665540085"
  data-width="1440" data-height="900" data-hostname="" data-title="呆萌可爱小<strong>猫咪</strong>电脑壁纸高清 动物壁纸" data-personalized="0" 
  data-partnerid="0"><div class="imgbox"><a href="/search/detail?ct=503316480&amp;z=undefined&amp;tn=baiduimagedetail&amp;ipn=d&amp;word=壁纸 
  动物 猫咪&amp;step_word=&amp;ie=utf-8&amp;in=&amp;cl=2&amp;lm=-1&amp;st=-1&amp;cs=472695846,665540085&amp;os=3712437847,360351780&amp;simid=3367675418,
  270123180&amp;pn=0&amp;rn=1&amp;di=97841061340&amp;ln=3992&amp;fr=&amp;fmq=1516240402890_R&amp;fm=rs2&amp;ic=undefined&amp;s=undefined&amp;se=&amp;sme=&amp;
  tab=0&amp;width=undefined&amp;height=undefined&amp;face=undefined&amp;is=0,0&amp;istype=0&amp;ist=&amp;jit=&amp;bdtype=0&amp;spn=0&amp;pi=0&amp;gsm=0&amp;
  oriquery=图片&amp;objurl=http%3A%2F%2Fwww.pp3.cn%2Fuploads%2F201505%2F2015051901.jpg&amp;rpstart=0&amp;rpnum=0&amp;adpicid=0" target="_blank" style="display: 
  block; width: 318px; height: 199px;" name="pn0" class="div_472695846,665540085"><img class="main_img img-hover" data-imgurl="http://img3.imgtn.bdimg.com/it/u=472695846,665540085&amp;
  fm=27&amp;gp=0.jpg" src="http://img3.imgtn.bdimg.com/it/u=472695846,665540085&amp;fm=27&amp;gp=0.jpg" style="background-color: rgb(182, 173, 173); width: 318px; height: 199px;"></a></div></li>

'''



