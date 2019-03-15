from moviepy.editor import *


video1 = VideoFileClip('/Users/ly/Desktop/Python/project/movie/IMG_0343.MP4').subclip(0,1500)
video2 = VideoFileClip('/Users/ly/Desktop/Python/project/movie/IMG_0343.MP4').subclip(1500,3000)
video3 = VideoFileClip('/Users/ly/Desktop/Python/project/movie/IMG_0343.MP4').subclip(3000,4500)
video4 = VideoFileClip('/Users/ly/Desktop/Python/project/movie/IMG_0343.MP4').subclip(4500,5610)
result1 = CompositeVideoClip([video1,])
result2 = CompositeVideoClip([video2,])
result3 = CompositeVideoClip([video3,])
result4 = CompositeVideoClip([video4,])

result1.to_videofile('/Users/ly/Desktop/Python/project/movie/movies/video1.MP4')
result2.to_videofile('/Users/ly/Desktop/Python/project/movie/movies/video2.MP4')
result3.to_videofile('/Users/ly/Desktop/Python/project/movie/movies/video3.MP4')
result4.to_videofile('/Users/ly/Desktop/Python/project/movie/movies/video4.MP4')



# #! /usr/bin/env python  
# #coding=utf-8  
# import cv2  
# import numpy as np  
# import cv2.cv as cv  
# videoCapture = cv2.VideoCapture("E://code//test.mp4") # 从文件读取视频  
# # 判断视频是否打开  
# if (videoCapture.isOpened()):  
#     print 'Open'  
# else:  
#     print 'Fail to open!'  
  
# fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)  #获取原视频的帧率  
  
# size = (int(600), int(1536))#自定义需要截取的画面的大小  
# #size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))#获取原视频帧的大小  
# videoWriter = cv2.VideoWriter('E://code//test2.avi', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)  
# success, frame = videoCapture.read()#读取第一帧  
  
# while success:  
#     frame = frame[0:1536,1200:1800]#截取画面  
#     videoWriter.write(frame)#将截取到的画面写入“新视频”  
#     success, frame = videoCapture.read()#循环读取下一帧  
# videoCapture.release()









