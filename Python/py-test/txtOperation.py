'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
使用 Python 生成类似于下图中的**字母验证码图片**
'''

# import os

# #读取.txt文件
# def read_txt(dir):
# 	with open(dir,'r') as f:
# 		return f.readlines()
# 	return ''

# #单词的总量
# dir = '/Users/ly/Desktop/test.txt'
# line_num = 0
# for line in read_txt(dir):
# 	words = str(line).split(' ')
# 	line_num += len(words)
# print(line_num)

# #单词出现的频率
# d = dict()
# for line in read_txt(dir):
# 	words = str(line).split(' ')
# 	for word in words:
# 		if str(word) in d:
# 			d[str(word)] += 1
# 		else:
# 			d[str(word)] = 1
# print(d)

# #统计字母在字符串中出现的次数
# set = set()
# test_string = 'eratyuiaopdaafaahjakaalxcvabnmeraatyuiaaofghjkcvbnamdfaghjaratyufaghjk'
# for s in test_string:
# 	set.add(s)
# set = set(test_string)
# for c in set:
# 	print(test_string.count(c))

# import time
# print('begin--', time.time())
# ss = ''
# for i in range(1000000):
# 	ss += test_string
# print('start for--', time.time())
# s1 = time.time()
# set1 = set()
# for s in ss:
# 	set1.add(s)
# print('end for--', time.time())
# e1 = time.time()
# print('start set--', time.time())
# s2 = time.time()
# set2 = set(ss)
# print('end set--', time.time())
# e2 = time.time()
# print(e1 - s1)#9.377879858016968
# print(e2 - s2)#1.0037169456481934
# '''
# 使用‘set2 = set(ss)’的效率是使用‘for s in ss: set1.add(s)’效率的9倍左右，
# 所以千万别随意使用for循环
# '''


# #获取各个txt的路径
# dir = '/Users/ly/Desktop/Python/py-test/txt-test'
# dict1 = dict()
# ignore = ['','\n','the','a','is','to','of','and','or','will','would','with','that']
# for d in os.listdir(dir):
# 	dict2 = dict()
# 	path = os.path.join(dir, d)
# 	with open(path, 'r') as f:
# 		for line in f.readlines():
# 			for word in line.split(' '):
# 				if word.lower() in ignore:
# 					continue
# 				if word in dict2:
# 					dict2[str(word)] += 1
# 				else:
# 					dict2[str(word)] = 1
# 		f.close()
# 	result = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
# 	dict1[str(path)] = result[:3]
# print(dict1)


# #计算项目代码总量
# dir = '/Users/ly/Desktop/qixiaofu/qixiaofu'
# #列出所有文件路径，递归
# def get_all_dirs(dir):
# 	list1 = []
# 	def all_dirs(dir):
# 		for d in os.listdir(dir):
# 			file = os.path.join(dir,d)
# 			if '.' in d:
# 				if d[d.rfind('.')+1:].lower() in ['swift']:
# 					list1.append(file)
# 			else:
# 				if os.path.isdir(file):
# 					all_dirs(file)
# 	all_dirs(dir)
# 	return list1
# l = get_all_dirs(dir)
# line_num = 0
# for s in l:
# 	with open(s,'r') as f:
# 		line_num += len(f.readlines())
# print(line_num)#37357



# #生成图片验证码
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random

# #rand light color 
# def randColor1():
# 	# return (random.randint(64,255), random.randint(64,255), random.randint(64,255))
# 	return (random.randint(64,180), random.randint(64,180), random.randint(64,180))
# #rand bravel color
# def randColor2():
# 	return (random.randint(64,127), random.randint(64,127), random.randint(64,127))
# #rand char
# def randChr():
# 	return chr(random.choice([random.randint(65,90), random.randint(97,122)]))

# font = ImageFont.truetype('Arial.ttf', 36)
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width,height), (255, 255, 255))
# draw = ImageDraw.Draw(image)
# for x in range(width):
# 	for y in range(height):
# 		draw.point((x,y), fill = randColor1())
# for i in range(4):
# 	c = randChr()
# 	draw.text((60 * i + 20, 10), c, font = font, fill=randColor2())
# image.save('/Users/ly/Desktop/Python/py-test/code_image.jpg')

# if 0.1 + 0.2 == 0.3:
# 	print(True)
# else:
# 	print(False)

# print(~5)
# 00000101
#111111010 -> 100000110

# print(~-100000000000)


# x = 12

# def f1():
# 	x = 3
# 	print(x)

# def f2():
# 	global x
# 	x += 1
# 	print(x)

# f1()
# f2()



#输入敏感字时变成*
# dir = '/Users/ly/Desktop/Python/py-test/txt-test/filtered_words.txt'
# list = []
# with open(dir, 'r') as f:
# 	for line in f.readlines():
# 		list.append(line.strip())
#	f.close()
# input = input('请输入...:')
# # if input in list:
# # 	print('Freedom')
# # else:
# # 	print('Human Rights')
# for word in list:
# 	n = ''
# 	for i in range(len(word)):
# 		n += '*'
# 	if word in input:
# 		input = input.replace(word,n)
# 	else:
# 		print('---')
# print(input)


# # python操作excel
# #写入excel
# import json
# import xlrd #读取数据
# import xlwt #写入数据
# import xlutils #操作excel

# dir = '/Users/ly/Desktop/Python/py-test/txt-test/student.txt'
# excel_file = r'/Users/ly/Desktop/Python/py-test/txt-test/stu.xls'
# s = ''
# with open(dir, 'r') as f:
# 	s = f.read()
# 	f.close()
# jsons = json.loads(s)
# row = len(jsons)
# clos = []
# for j in jsons:
# 	clos.append(len(jsons[j]))
# clo = max(clos)
# #对excel的写操作
# # 创建一个Workbook对象，这就相当于创建了一个Excel文件
# '''
# Workbook类初始化时有encoding和style_compression参数
# encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
# 默认是ascii。当然要记得在文件头部添加：
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# style_compression:表示是否压缩，不常用。
# '''
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# #创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# '''
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
# '''
# sheet = book.add_sheet('student', cell_overwrite_ok=True)
# # 向表test中添加数据
# #1.表头
# titles = ['序号','姓名','数学','物理','化学']
# for i in range(clo + 1):
# 	sheet.write(0,i,titles[i])
# index = 1
# for j in jsons:
# 	sheet.write(index,0,j)
# 	jj = jsons[j]
# 	for i in range(row):
# 		sheet.write(index,i+1,jj[i])
# 	index += 1
# book.save(excel_file)


# #读取excel
# book = xlrd.open_workbook(excel_file)#得到Excel文件的book对象，实例化对象
# sheet1 = book.sheet_by_index(0)# 通过sheet索引获得sheet对象
# print(sheet1)#<xlrd.sheet.Sheet object at 0x1048a0550>
# sheet_name = book.sheet_names()[0]# 获得指定索引的sheet表名字
# print(sheet_name)
# # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
# sheet2 = book.sheet_by_name(sheet_name)
# rows = sheet2.nrows# 获取行总数
# print(rows)
# # 获得第1行的数据列表
# print(sheet2.row_values(0))
# # 获得第1列的数据列表
# print(sheet2.col_values(0))
# # 通过坐标读取表格中的数据
# cols = sheet2.ncols
# for x in range(rows):
# 	for y in range(cols):
# 		print(sheet2.cell_value(x,y))




# sss = '''
#     {
#         "1" : "上海",
#         "2" : "北京",
#         "3" : "成都"
#     }
# # '''
# sss = '''
#     [
#     	[1, 82, 65535], 
#     	[20, 90, 13],
#     	[26, 809, 1024]
#     ]
# '''
# j = json.loads(sss)
# for jj in j:
# 	print(j)



































