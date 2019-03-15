'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''

import os
from PIL import Image

from datetime import datetime

def resize_pic(dir, width, height):
	#建立新的文件夹
	new_path = os.path.join(dir, datetime.now().strftime('%Y%m%d'))
	if os.path.exists(new_path):
		for f in os.listdir(new_path):
			fi = os.path.join(new_path, f)
			os.remove(fi)
		os.rmdir(new_path)
	os.mkdir(new_path)
	#获取图片文件
	for f in os.listdir(dir):
		suffix = f[f.rfind('.') + 1 :]
		if suffix in ['jpeg', 'jpg', 'png']:
			file = os.path.join(dir, f)
			pic = Image.open(file)
			new_file = os.path.join(new_path, f)
			if pic.size[0] > width or pic.size[1] > height:
				# pic.thumbnail((width, height))
				out = pic.resize((width, height))
			# pic.save(new_file)
			out.save(new_file)

file_path = '/Users/ly/Desktop/Python/py-test/20180108'
resize_pic(file_path, 200, 250)



