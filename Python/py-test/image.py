'''
python练手项目
# https://www.zhihu.com/question/29372574   

python 小程序
https://github.com/Yixiaohan/show-me-the-code
'''

#20180110
'''
0、将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。
'''

from PIL import Image, ImageDraw, ImageFont

#添加对角线
'''
draw.arc(xy, start, end, options)
含义：在给定的区域内，在开始和结束角度之间绘制一条弧（圆的一部分）。
变量options中fill设置弧的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# print(im.size)
# draw = ImageDraw.Draw(im)
# draw.line((0,0) + im.size, fill = 28)
# draw.line((im.size[1],0) + (0,im.size[0]), fill = 200 )
# im.show()
# del draw

#添加弧角
'''
draw.arc(xy, start, end, options)
变量xy是需要设置一个区域，此处使用4元组，包含了区域的左上角和右下角两个点的坐标。
弧都是按照顺时针方向绘制的
可绘制圆以及椭圆
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.arc((0,0,200,200),0,90,fill = 222)#圆
# draw.arc((200,200,400,500),0,-90,fill = 222)#椭圆
# draw.arc((200,200,300,300),-90,0,fill = 222)#圆
# im.show()
# del draw

 # Pieslice
'''
定义：draw.pieslice(xy,start, end, options)
含义：和方法arc()一样，但是在指定区域内结束点和中心点之间绘制直线。
变量options的fill给定pieslice内部的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.pieslice((0,0,200,200),0,90,fill = 222)#扇形
# draw.pieslice((200,200,400,500),0,-90,fill = 222)#椭圆扇形
# draw.pieslice((200,200,300,300),-90,0,fill = 222)#圆扇形
# im.show()
# del draw

# Chord
'''
定义：draw.chord(xy,start, end, options)
含义：和方法arc()一样，但是使用直线连接起始点。
变量options的outline给定弦轮廓的颜色。Fill给定弦内部的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.chord((0,0,200,200),0,90,fill=128,outline=222)
# im.show()
# del draw

# Ellipse
'''
定义：draw.ellipse(xy,options)
含义：在给定的区域绘制一个椭圆形。
变量options的outline给定椭圆形轮廓的颜色。Fill给定椭圆形内部的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.ellipse((0,0,200,200),fill=123)
# draw.ellipse((200,200,300,400),fill=123)
# im.show()
# del draw

# Polygon
'''
定义：draw.polygon(xy,options)
含义：绘制一个多边形。
多边形轮廓由给定坐标之间的直线组成，在最后一个坐标和第一个坐标间增加了一条直线，形成多边形。
坐标列表是包含2元组[(x,y),…]或者数字[x,y,…]的任何序列对象。它最少包括3个坐标值。
变量options的fill给定多边形内部的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.polygon([(0,0),(100,50),(50,100)],fill=123)
# draw.polygon([0,20,50,90,100,300,200,80],fill=222)
# im.show()
# del draw

# Rectangle
'''
定义：draw.rectangle(box,options)
含义：绘制一个长边形。
变量box是包含2元组[(x,y),…]或者数字[x,y,…]的任何序列对象。它应该包括2个坐标值。
注意：当长方形没有没有被填充时，第二个坐标对定义了一个长方形外面的点。
变量options的fill给定长边形内部的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.rectangle([(0,0),(100,120)],fill=123)
# draw.rectangle((120,130,200,180),fill=222)
# draw.rectangle([200,200,300,400],fill=150)
# im.show()
# del draw

# Bitmap
'''
draw.bitmap(xy, bitmap, options)
含义：在给定的区域里绘制变量bitmap所对应的位图，非零部分使用变量options中fill的值来填充。变量bitmap位图应该是一个有效的透明模板（模式为“1”）或者蒙版（模式为“L”或者“RGBA”）。
这个方法与Image.paste(xy, color, bitmap)有相同的功能。
'''
# im1 = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# im2 = Image.open('/Users/ly/Desktop/Python/py-test/image3.png')
# im = im2.resize((80,100),Image.ANTIALIAS)
# print(im.size)
# r,g,b = im.split()
# draw = ImageDraw.Draw(im1)
# draw.bitmap((0,0),r,fill=111)
# draw.bitmap((80,100),g,fill=(0,255,0))
# draw.bitmap((160,200),b,fill=(0,0,255))
# im1.show()
# del draw

 # Line
'''
定义：draw.line(xy,options)
含义：在变量xy列表所表示的坐标之间画线。
坐标列表可以是任何包含2元组[(x,y),…]或者数字[x,y,…]的序列对象。它至少包括两个坐标。
变量options的fill给定线的颜色。
（New in 1.1.5）变量options的width给定线的宽度。注意线连接不是很好，所以多段线段连接不好看。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.line([(0,0),(100,50),(50,100)],fill=123,width=3)
# draw.line([0,20,50,90,100,300,200,80],fill=222,width=10)
# im.show()
# del draw

# Point
'''
定义：draw.point(xy,options)
含义：在给定的坐标点上画一些点。
坐标列表是包含2元组[(x,y),…]或者数字[x,y,…]的任何序列对象。
变量options的fill给定点的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.point((100,100),fill=123)
# draw.point((101,101),fill=(0,0,0))
# im.show()
# del draw

# Text
'''
定义：draw.text(position,string, options)
含义：在给定的位置绘制一个字符创。变量position给出了文本的左上角的位置。
变量option的font用于指定所用字体。它应该是类ImangFont的一个实例，使用ImageFont模块的load()方法从文件中加载的。
变量options的fill给定文本的颜色。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# draw.text((im.size[1]-100,100),'haha',fill=(255,0,0),font=ImageFont.truetype('/Users/ly/Desktop/Python/py-test/image.ttf'))
# draw.text((100,100),'hahahah',font=ImageFont.truetype('Arial/Arial.ttf',46))
# im.show()
# del draw

# Textsize
'''
定义：draw.textsize(string,options)⇒ (width, height)
含义：返回给定字符串的大小，以像素为单位。
变量option的font用于指定所用字体。它应该是类ImangFont的一个实例，使用ImageFont模块的load()方法从文件中加载的。
'''
# im = Image.open('/Users/ly/Desktop/Python/py-test/image.jpg')
# draw = ImageDraw.Draw(im)
# print(draw.textsize('haha'))
# print(draw.textsize('hello word'))
# del draw



# #为图片添加水印
# # 加载中间透明的手机图片
# base_img = Image.open('/Users/ly/Desktop/Python/py-test/test.png')
# #新建透明底图，大小和手机图一样，mode使用RGBA，保留Alpha透明度，颜色为透明
# #Image.new(mode, size, color=0)，color可以用tuple表示，分别表示RGBA的值
# target = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
# box = (0, 0, base_img.size[0]-100, base_img.size[1]-100) #区域
# region = Image.open('/Users/ly/Desktop/Python/py-test/watermark.png')
# scaler = Image.ANTIALIAS

# #确保图片是RGBA格式，大小和box区域一样
# # region = region.convert("RGBA")
# region = region.resize((box[2] - box[0], box[3] - box[1]))
# #先将狐狸像合成到底图上
# # target.paste(region,box)
# #将手机图覆盖上去，中间透明区域将狐狸像显示出来。
# #第一个参数表示需要粘贴的图像，中间的是坐标，最后是一个是mask图片，用于指定透明区域，将底图显示出来。
# target.paste(base_img,(0,0),base_img)
# # target.show()
# target.paste(region,box)
# target.show()

# #为图片添加水印
# # 加载中间透明的手机图片
# base_img = Image.open('/Users/ly/Desktop/Python/py-test/test.png')
# #新建透明底图，大小和手机图一样，mode使用RGBA，保留Alpha透明度，颜色为透明
# #Image.new(mode, size, color=0)，color可以用tuple表示，分别表示RGBA的值
# target = Image.new('RGBA', base_img.size, (0, 0, 0, 0))
# box = (0, 0, base_img.size[0]-100, base_img.size[1]-100) #区域
# region = Image.open('/Users/ly/Desktop/Python/py-test/watermark.png')

# #确保图片是RGBA格式，大小和box区域一样
# region = region.convert("RGBA")
# region = region.resize((box[2] - box[0], box[3] - box[1]))
# img_blender = Image.new('RGBA', region.size, (0,0,0,0))  
# region = Image.blend(img_blender, region, 0.5) 

# #先将狐狸像合成到底图上
# # 将手机图覆盖上去，中间透明区域将狐狸像显示出来。
# # 第一个参数表示需要粘贴的图像，中间的是坐标，最后是一个是mask图片，用于指定透明区域，将底图显示出来。
# # target.show()
# target.paste(base_img,(0,0),base_img)
# # target.show()
# target.paste(region,box)
# target.show()



# watermark = Image.open('/Users/ly/Desktop/Python/py-test/watermark.png')
# watermark = watermark.resize((300,300))
# imageFile = Image.open('/Users/ly/Desktop/Python/py-test/test.png')
# layer = Image.new('RGBA', imageFile.size, (0,0,0,0))
# layer.paste(watermark, (imageFile.size[0]-300, imageFile.size[1]-80))
# out=Image.composite(layer,imageFile,layer)
# out.show()



