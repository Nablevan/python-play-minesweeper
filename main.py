import numpy as np
import cv2
import win32gui
import time
# import win32api
from PIL import ImageGrab
from pymouse import PyMouse

class_name = "TMain"
title_name = "Minesweeper Arbiter "
# 获取句柄
hwnd = win32gui.FindWindow(class_name, title_name)
# 获取窗口左上角和右下角坐标
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left)
window = win32gui.GetWindowRect(hwnd)
original_point = [window[0]+15, window[1]+101]  # 雷区原点位置，每块16*16像素

m = PyMouse()
m.click(original_point[0], original_point[1], button=1)

# 雷块色值：0[192,192,192]
#          1[0,0,255]
#          2[0,128,0]
#          3[255,0,0]
#          4[0,0,128]
#          5[128,0,0]
#          6[0,128,128]
#          7[0,0,0]   正常模式不出现
#          8[128,128,128]   正常模式不出现
#          未翻开(0,0)位置色值[255,255,255]
#          已翻开(0,0)位置色值[128,128,128]
#
# 屏幕抓取
# start_time = time.time()
# while True:
#     screen = cv2.cvtColor(np.array(ImageGrab.grab(window)), cv2.COLOR_BGR2RGB)
#     cv2.imshow('window', screen)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#     print('loop time {}'.format(time.time()-start_time))
#     start_time = time.time()
