'''
分析：播放指定video视频，esc键退出播放
'''
import numpy as np
import cv2
import time

videoName = 'viplanedeparture.avi'

print(videoName)

videoCapture = cv2.VideoCapture(videoName)

print('is open?', videoCapture.isOpened())

fps = videoCapture.get(cv2.CAP_PROP_FPS)
print('fps:', fps)


success, frame = videoCapture.read()
print(ord('a'))

while success:
    cv2.imshow('video', frame)
    if cv2.waitKey(int(1000 / fps)) & 0xFF == 27: #27: escape, or use ord('q') for key 'q'
        break
    success, frame = videoCapture.read() 
    




    