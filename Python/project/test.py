



#批量更改名字
# import os
# from datetime import datetime
# def changeName(filePath, name):
# 	files = os.listdir(filePath)
# 	for i in range(len(files)):
# 		file = os.path.join(filePath,files[i])	
# 		if '.' in files[i]:
# 			pos = files[i].rindex('.')
# 			suffix = files[i][pos:]
# 			if suffix.lower() in ['.png', '.jpeg', '.jpg']:
# 				new = os.path.join(filePath,name+str(i)+suffix.lower())
# 				os.rename(file,new)
# filePath = '/Users/ly/Desktop/Python/picture/20180116'
# changeName(filePath,'jianshu')

#批量更改名字
# import os
# from datetime import datetime
# def changeName(filePath, name):
# 	now = datetime.now()
# 	newPath = os.path.join(filePath, now.strftime('%Y%m%d'))
# 	if os.path.exists(newPath):
# 		for fi in os.listdir(newPath):
# 			os.remove(os.path.join(newPath,fi))
# 		os.rmdir(newPath)
# 	os.mkdir(newPath)
# 	files = os.listdir(filePath)
# 	for i in range(len(files)):
# 		file = os.path.join(filePath,files[i])	
# 		if '.' in files[i]:
# 			pos = files[i].rindex('.')
# 			suffix = files[i][pos:]
# 			if suffix.lower() in ['.png', '.jpeg', '.jpg']:
# 				with open(file, 'rb') as f1:
# 					new = os.path.join(newPath,name+str(i)+suffix.lower())
# 					with open(new,'ab') as f2:
# 						f2.write(f1.read())
# 						f2.close()
# 						print(i)
# filePath = '/Users/ly/Desktop/Python/picture'
# changeName(filePath,'jianshu')



# import asyncio
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。
# async def wget(host):
# 	print('wget %s...' % host)
# 	connect = asyncio.open_connection(host, 80)
# 	reader, writer = await connect
# 	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
# 	writer.write(header.encode('utf-8'))
# 	await writer.drain()
# 	while True:
# 		line = await reader.readline()
# 		if line == b'\r\n':
# 			break
# 		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
# 	writer.close()
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#插入排序
# def insertSort(arr):
# 	for i in range(len(arr)):
# 		preIndex = i - 1
# 		current = arr[i]
# 		while preIndex >= 0 and arr[preIndex] > current:
# 			arr[preIndex + 1] = arr[preIndex]
# 			preIndex -= 1
# 		arr[preIndex + 1] = current
# 	return arr


#协程
# def consumer():
# 	r = ''
# 	while True:
# 		n = yield r
# 		if not n :
# 			return
# 		print('Consumer %s...' % n)
# 		r = '200 OK'
# def produce(c):
# 	c.send(None)
# 	n = 0
# 	while n < 5:
# 		n += 1
# 		print('Producing %s...' % n)
# 		r = c.send(n)
# 		print('Consumer return %s...' % r)
# 	c.close()
# c = consumer()
# produce(c)
# consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务






#2017-12-28

# import socket
# # ####服务端######
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #绑定端口
# s.bind(('127.0.0.1', 9999))
# print('bind UDP on 9999...')
# while True:
# 	#接收数据
# 	data, addr = s.recvfrom(1024)
# 	print('received from %s:%s' % addr)
# 	s.sendto(b'hello, %s' % data, addr)
# ####客户端######
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in [b'Michael', b'Tracy', b'Sarah', b'ly', b'wj', b'lw', b'hah']:
# 	#发送数据
# 	s.sendto(data, ('127.0.0.1', 9999))
# 	#接收数据
# 	print(s.recv(1024).decode('utf-8'))
# s.close()


# # 导入socket库:
# import socket, time, threading
# ####服务端######
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 9999))#监听端口
# s.listen(5)
# print('Watting for connection ...')

# def tcplink(sock, addr):
# 	print('Aaccept new connection from %s:%s' % (addr))
# 	sock.send(b'Welcom!')
# 	while True:
# 		data = sock.recv(1024)
# 		time.sleep(1)
# 		if not data or data.decode('utf-8') == 'exit':
# 			break
# 		sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
# 	sock.close()
# 	print('connection from %s:%s closed' % addr)

# while True:
# 	#接受一个新链接
# 	sock, addr = s.accept()
# 	#创建新的线程来处理tcp链接
# 	t = threading.Thread(target=tcplink, args=(sock, addr))
# 	t.start()
# ####客户端######
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #建立连接
# s.connect(('127.0.0.1', 9999))
# #接受欢迎消息
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah', b'ly', b'wj', b'lw']:
# 	s.send(data)
# 	print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()



# # 导入socket库:
# import socket
# # 创建一个socket: AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接:
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('/Users/ly/Desktop/Python/project/sina.html', 'wb') as f:
#     f.write(html)

# from tkinter import *
# import tkinter.messagebox as messagebox
# class Application(Frame):
# 	def __init__(self, master = None):
# 		Frame.__init__(self, master)
# 		self.pack()
# 		self.createWidgets()
# 	def createWidgets(self):
# 		self.helloLabel = Label(self, text = 'Hello, word!')
# 		self.helloLabel.pack()
# 		self.quitButton = Button(self, text='Quit', command = self.quit)
# 		self.quitButton.pack()
# app = Application()
# app.master.title('hahhahahahah')
# app.mainloop()
# class Application(Frame):
# 	def __init__(self, master = None):
# 		Frame.__init__(self, master)
# 		self.pack()
# 		self.createWidgets()
# 	def createWidgets(self):
# 		self.nameInput = Entry(self)
# 		self.nameInput.pack()
# 		self.alertButton = Button(self, text = 'Hello', command = self.hello)
# 		self.alertButton.pack()
# 	def hello(self):
# 		name = self.nameInput.get() or 'word'
# 		messagebox.showinfo('Message', 'Hello, %s' % name)
# app = Application()
# app.master.title('hello')
# app.mainloop()



# import chardet
# print(chardet.detect(b'hello, world'))
# data = '离离原上草，一岁一枯荣'.encode('gbk')
# print(chardet.detect(data))

# from PIL import Image, ImageFilter
#改变图片尺寸
# im = Image.open('icon19.jpg')
# w,h = im.size
# print('Origin image size:%s X %s' % (w,h))
# # 缩放到50%:
# im.thumbnail((w//2,h//2))
# print('Resize image to : %s X %s' % (w//2,h//2))
# im.save('thumbnail.jpg', 'jpeg')
# 图片模糊效果
# im = Image.open('icon19.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2 = im2.filter(ImageFilter.BLUR)
# im2.save('blur2.jpg', 'jpeg')
#生成字母验证码图片
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# #随机字母
# def rndChar():
# 	return chr(random.randint(65,90))
# #随机颜色 浅色
# def rndColor1():
# 	return (random.randint(64,255), random.randint(64,255), random.randint(64,255))
# #随机颜色 深色
# def rndColor2():
# 	return (random.randint(32,127), random.randint(32,127), random.randint(32,127))
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# font = ImageFont.truetype('Arial.ttf', 36)
# draw = ImageDraw.Draw(image)
# for x in range(width):
# 	for y in range(height):
# 		draw.point((x, y), fill = rndColor1())
# for t in range(4):
# 	draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())
# image = image.filter(ImageFilter.BLUR)
# image.save('code.png','png')


# import psutil
# print(psutil.cpu_count())# CPU逻辑数量
# print(psutil.cpu_count(logical=False))# CPU物理核心
# print(psutil.cpu_times())#统计CPU的用户／系统／空闲时间
# # 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# for i in range(10):
# 	print(psutil.cpu_percent(interval=1, percpu=True))
# # 使用psutil获取物理内存和交换内存信息
# print(psutil.virtual_memory())
# print(psutil.swap_memory())
# #通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
# print(psutil.disk_partitions())
# print(psutil.disk_usage('/'))
# print(psutil.disk_io_counters())
# print(psutil.net_io_counters())#获取网络读写字节／包的个数
# print(psutil.net_if_addrs())# 获取网络接口信息
# print(psutil.net_if_stats())# 获取网络接口状态
'''
net_connections() 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，
而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动
'''
# print(psutil.net_connections())#当前网络连接信息
# print(psutil.pids())#所有进程ID
# print(psutil.Process(61))# 获取指定进程ID=61，其实就是当前Python交互环境
'''
>>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
>>> p.name() # 进程名称
'python3.6'
>>> p.exe() # 进程exe路径
'/Users/michael/anaconda3/bin/python3.6'
>>> p.cwd() # 进程工作目录
'/Users/michael'
>>> p.cmdline() # 进程启动的命令行
['python3']
>>> p.ppid() # 父进程ID
3765
>>> p.parent() # 父进程
<psutil.Process(pid=3765, name='bash') at 4503144040>
>>> p.children() # 子进程列表
[]
>>> p.status() # 进程状态
'running'
>>> p.username() # 进程用户名
'michael'
>>> p.create_time() # 进程创建时间
1511052731.120333
>>> p.terminal() # 进程终端
'/dev/ttys002'
>>> p.cpu_times() # 进程使用的CPU时间
pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
>>> p.memory_info() # 进程使用的内存
pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
>>> p.open_files() # 进程打开的文件
[]
>>> p.connections() # 进程相关网络连接
[]
>>> p.num_threads() # 进程的线程数量
1
>>> p.threads() # 所有线程信息
[pthread(id=1, user_time=0.090318, system_time=0.062736)]
>>> p.environ() # 进程环境变量
{'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
>>> p.terminate() # 结束进程
Terminated: 15 <-- 自己把自己结束了
'''


# 强烈推荐安装Anaconda，安装后，数十个常用的第三方模块就已经就绪


# from urllib import request, parse
# print('Login to weibo.cn...')
# email = input('EmailOrPhone: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# 	data = f.read()
# 	print('Status: ', f.status, f.reason)
# 	for k, v in f.getheaders():
# 		print('%s: %s' % (k, v))
# 	print('Data: ', data.decode('utf-8'))


# from contextlib import closing, contextmanager
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
# import itertools
# count()会创建一个无限的迭代器，所以下面代码会打印出自然数序列
# natuals = itertools.count(1)
# for n in natuals:
# 	print(n)
# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('abc')
# for c in cs:
# 	print(c)
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('A',11)
# ns = itertools.repeat('A')
# for n in ns:
# 	print(n)
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x < 10, natuals)
# print(list(ns))
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', '123', '~.,'):
# 	print(c)
# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby('AAABBBCCCCCCAA'):
# 	print(key,list(group))

# import hmac
# s = b'how to use hmac in python hashlib'
# s1 = b'how to use hmac '
# s2 = b'in python hashlib'
# key = b'secret'
# h = hmac.new(key, s, digestmod='MD5')
# print(h.hexdigest())
# h2 = hmac.new(key, s1, digestmod='MD5')
# h2.update(s2)
# print(h2.hexdigest())
# # 9104c474395511d7d38784b690179b35
# # 9104c474395511d7d38784b690179b35

# import hashlib
# md5 = hashlib.md5()
# # md5.update('how to use md5 in python hashlib'.encode('utf-8'))
# # print(md5.hexdigest())
# md5.update('how to use md5'.encode('utf-8'))
# md5.update(' in python hashlib'.encode('utf-8'))
# print(md5.hexdigest())
# sha1 = hashlib.sha1()
# sha1.update('how to use md5'.encode('utf-8'))
# sha1.update(' in python hashlib'.encode('utf-8'))
# print(sha1.hexdigest())

# import base64, struct
# def bmp_info(data):
# 	t = struct.unpack('<ccIIIIIIHH',data)
# 	if t[0] == b'B' and (t[1] == b'M' or t[1] == b'A'):
# 		return{
# 			'width' : t[6],
# 			'height' : t[7],
# 			'color' : t[9]
# 		}
# 	return{
# 		'width' : 0,
# 		'height' : 0,
# 		'color' : 0
# 	}
# bmp_data = base64.b64decode('''
# Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCw
# AAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//
# f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AH
# wAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9/
# /3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/
# 9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwA
# fP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38
# AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3
# //f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/
# 3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/
# AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/
# AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8
# AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8
# AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9/
# /3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==''')
# d = bmp_info(bmp_data[:30])
# print(d['height'])

# import struct
# n = 10240099
# print(struct.pack('>I', n))
# b1 = b'\xf0\xf0\xf0\xf0\x80\x80'
# b2 = b'\x00\x9c@c'
# print(struct.unpack('>I',b2))
# print(struct.unpack('>IH',b1))

# n = 10240099
# b1 = (n & 0xff000000) >> 24
# print(b1)
# b2 = (n & 0xff0000) >> 16
# print(b2)
# b3 = (n & 0xff00) >> 8
# print(b3)
# b4 = (n & 0xff) 
# print(b4)
# bs = bytes([b1,b2,b3,b4])
# print(bs)
# print(bytes([b1]))
# print(bytes([b2]))
# print(bytes([b3]))
# print(bytes([b4]))
# print(bin(10240099))#0b 1001 1100 0100 0000 1100 011

# import base64
# print(base64.b64encode(b'1'))
# print(base64.b64encode(b'abc'))
# print(base64.b64decode('YWJj'))

# from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# Circle = namedtuple('Circle',['x', 'y', 'r'])
# circle = Circle(1,2,3)
# print(circle.y)

# q = deque(['a', 'b', 'c'])
# q.append('x')
# print(q)
# q.appendleft('y')
# print(q)
# q.popleft()
# print(q)
# q.pop()
# print(q)

# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'nnn'
# print(dd['key1'])
# print(dd['key2'])

#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序,可以实现一个FIFO（先进先出）的dict，
#当容量超出限制时，先删除最早添加的Key
# od = OrderedDict()
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# print(od)

#Counter是一个简单的计数器，例如，统计字符出现的个数
# c = Counter()
# for ch in 'merry christmas':
# 	c[ch] += 1
# print(c)


# from datetime import datetime, timedelta, timezone
# dt = datetime(2017,12,25,10,40,46)
# print(dt)
# print(dt.timestamp())
# t = 1514169646.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))
# cday = datetime.strptime('2017-12-25 11:05:21', '%Y-%m-%d %H:%M:%S')
# print(cday)
# now = datetime.now()
# print(now.strftime('%a, %b %Y %d %H:%M'))
# now = datetime.now()
# now += timedelta(hours = 10)
# print(now)
# now += timedelta(days = 1, minutes = 20)
# print(now)
# now -= timedelta(seconds = 23)
# print(now)
# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)
# # 拿到UTC时间，并强制设置时区为UTC+0:00:
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# # astimezone()将转换时区为北京时间:
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# # astimezone()将转换时区为东京时间:
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# # astimezone()将bj_dt转换时区为东京时间:
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)
# def str2Date(timeStr,timeZone):
# 	dt = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
# 	dt2 = dt.astimezone(timezone(timedelta(hours=int(timeZone))))
# 	print(dt2)
# 	return dt2.timestamp()
# ts = str2Date('2017-12-25 12:00:30','5')
# print(ts)


# import re
# # list = re.split(r'\s+', 'a b    c')
# list = re.split(r'[\s\,\;]+', 'a,,, b ;;   c,d')
# print(list)

# re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')

# groups = re_tel.match('000-123123').groups()
# print(groups)


#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，
#互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

# import time, threading

# lock = threading.Lock()

# def loop():
# 	try:
# 		lock.acquire()
# 		print('thread %s is runing...' % threading.current_thread().name)
# 		n = 0
# 		while n < 5:
# 			n += 1
# 			print('thread %s >>> %s' % (threading.current_thread().name, n))
# 			time.sleep(1)
# 		print('thread %s ended' % threading.current_thread().name)
# 	finally:
# 		lock.release()
	

# print('thread %s is runing' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)


# from multiprocessing import Process, Queue
# import os, time, random
# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		time.sleep(random.random())

# def read(q):
# 	print('Process to read: %s' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue' % value)

# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write,args=(q,))
# 	pr = Process(target=read,args=(q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()


# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.qixiaofu.com'])
# print('Wxit code:', r)
# r = subprocess.call(['python3','/Users/ly/Desktop/ttt.py'])
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:',p.returncode)



# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
# 	print('Run task %s (%s)' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds' % (name,(end - start)))

# if __name__ == '__main__':
# 	print('Parent process %s' % os.getpid())
# 	p = Pool(4)#设置同时进行的进程数
# 	#p = Pool()#同时进行的进程数默认为cpu核数
# 	for i in range(10):
# 		p.apply_async(long_time_task, args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done')

# from multiprocessing import Process
# import os
# def run_proc(name):
# 	print('Run child process %s (%s)' % (name,os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process is %s' % os.getpid)
# 	p = Process(target=run_proc, args=('test',))
# 	print('Child process will start.')
# 	p.start()
# 	print('----')
# 	p.join()
# 	print('Child process end')

# import os
# print(os.getpid())

# pid = os.fork()
# if pid == 0:
# 	print('child process(%s),parent process(%s)' % (os.getpid(), os.getppid()))
# else:
# 	print('I(%s) create a child process(%s)' % (os.getpid(),pid))

# import json 

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
# s = Student('Bob', 20, 88)
# str = json.dumps(s,default=lambda obj:obj.__dict__)
# print(str)
# def dict2stu(d):
# 	return Student(d['name'],d['age'],d['score'])
# json_str = '{"name": "Bob", "age": 20, "score": 88}'
# s = json.loads(json_str, object_hook=dict2stu)
# print(s)
# print(s.__repr__)
# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True) #{"name": "\u5c0f\u660e", "age": 20}
# s = json.dumps(obj, ensure_ascii=False) #{"name": "小明", "age": 20}
# print(s)
# d = dict(name='ly', age=25, score=100)
# s = json.dumps(d)
# if isinstance(s,str):
# 	print('---')
# print(s)

# json_str = '{"name": "ly", "age": 25, "score": 100}'
# d = json.loads(json_str)
# if isinstance(d,dict):
# 	print('----')
# print(d)


# import pickle
'''
序列化存储
'''
# d = dict(name='ly', age='25', score=100)
# f = open('/Users/ly/Desktop/test.txt','wb')
# pickle.dump(d,f)
# f.close()
'''
反序列化
'''
# f = open('/Users/ly/Desktop/test.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)


# import shutil
# shutil.copyfile('/Users/ly/Desktop/test.txt','/Users/ly/Desktop/test333.txt')

# import os
# list = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(list)
# list = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.putty']
# print(list)
# print(os.path.split('/Users/ly/Desktop/test.txt')) #('/Users/ly/Desktop', 'test.txt')
# print(os.path.splitext('/Users/ly/Desktop/test.txt')) #('/Users/ly/Desktop/test', '.txt')
# print(os.path.splitext('/Users/ly/Desktop/test')) #('/Users/ly/Desktop/test', '')
# print(os.path.abspath('.'))
# print(os.path.join('/Users/ly', 'testdir'))
# print(os.path.join('/Users/ly', 'testdir'))
# os.mkdir('/Users/ly/testdir')
# os.rmdir('/Users/ly/testdir')
# print(os.name)
# print(os.uname())
# path = os.environ
# print(path['PATH'])
# print(path.get('TERM_SESSION_ID'))
# print(path.get('x', 'default'))

# from io import BytesIO
# f = BytesIO()
# f.write('中 wen'.encode('utf-8'))
# print(f.getvalue())

# from io import StringIO
# f = StringIO('hello!\nHI\nword')
# print(f.getvalue())
# print('---')
# for line in f.readlines():
# 	print(line)
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('word')
# print(f.getvalue())

# /Users/ly/Desktop/qixiaofu.png 
# /Users/ly/Desktop/test.txt

# f = open('/Users/ly/Desktop/test.txt','w')
# f.write('hahaha,hello ')
# f.write('\n')
# f.write('hahaha,hello ')
# f.close()
# with open('/Users/ly/Desktop/qixiaofu.png', 'rb') as f:
# 	print(f.read())

# with open('/Users/ly/Desktop/test.txt', 'r') as f:
# 	print(f.read(100))

# with open('/Users/ly/Desktop/test.txt', 'r') as f:
# 	for line in f.readlines():
# 		print(line)

# try:
# 	f = open('/Users/ly/Desktop/test.txt','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()


# # python3 -m pdb test.py 单步调试 ‘n’执行下一步
# s = '0'
# n = int(s)
# print(n * 2)


# from functools import reduce

# def str2num(s):
#     return float(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()


# from enum import Enum, unique

# @unique
# class WeekDay(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6

# print(WeekDay.Thu)
# print(WeekDay.Fri.value)		


# class Chain(object):

# 	def __init__(self, path=''):
# 		self._path = path

# 	def __getattr__(self, path):
# 		return Chain('%s/%s' % (self._path, path))

# 	def __str__(self):
# 		return self._path

# 	__repr__ = __str__
		
# l = Chain().status.user.timeline.list
# print(l)

# class Chain(object):

# 	def __init__(self, path=''):
# 		self._path = path

# 	def __getattr__(self, path):
# 		if path == 'users':
# 			return lambda name: Chain('%s/%s/:%s' % (self._path, path, name))
# 		else:
# 			return Chain('%s/%s' % (self._path, path))

# 	def __str__(self):
# 		return self._path

# 	__repr__ = __str__

# l = Chain().status.user.timeline.list
# print(l)
# l2 = Chain().users('ly').repos
# print(l2)

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
# 	return t[1]
# list = sorted(L,key=by_name)
# list = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# print(list)


# def intEqualInvertInt(num):
# 	num2 = int(str(num)[::-1])
# 	return num == num2

# l = list(filter(intEqualInvertInt, [x for x in range(1000)]))
# print(l)

# L1 = ['adam', 'LISA', 'barT']
# def transStr(str):
# 	str2 = ''
# 	for i in range(len(str)):
# 		if i == 0:
# 			str2 += str[i].upper()
# 		else:
# 			str2 += str[i].lower()
# 	return str2
# L2 = list(map(transStr,L1))
# print(L2)


#杨辉三角形
# def triangles(max):
# 	n = 0
# 	list = []
# 	while n < max:
# 		temp = []
# 		for num in range(len(list)):
# 			if num == 0:
# 				temp.append(list[num])
# 			else:
# 				temp.append(list[num-1] + list[num])
# 		temp.append(1)
# 		list = temp
# 		# print(list)
# 		yield list
# 		n += 1
# 	return 'done'
 
# t = triangles(10)
# for li in t:
# 	print(li)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str)]
# print(L2)

# import math 
# print ('{:.0f}'.format(math.pi))

# import sys
# print("命令行参数:")
# for i in sys.argv:
# 	print(i)

# print("\n\npython 路径:", sys.path,'\n')


# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()


# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num) 
#     num = 123
#     print(num)
# fun1()

# print(num)


# list = [1,2,3,4]
# it = iter(list)
# print (next(it))
# print (next(it),end='')
# print ('11111')
# for i in it:
# 	print(i)
# for i in list:
# 	print(i)

# import sys
# def fibonacci(n):
# 	a,b,counter = 0,1,0
# 	while True:
# 		if (counter > n):
# 			return
# 		yield a
# 		a,b = b,a + b
# 		counter += 1
# f = fibonacci(10)
# print(f)
# while True:
# 	try:
# 		print (next(f),end=' ')
# 	except StopIteration:
# 		sys.exit()



###########
##  end  ##
###########

