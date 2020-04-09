import numpy as np
import cv2
import win32gui
import time
# import win32api
from PIL import ImageGrab


class_name = "TMain"
title_name = "Minesweeper Arbiter "
# 获取句柄
hwnd = win32gui.FindWindow(class_name, title_name)
# 获取窗口左上角和右下角坐标
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left)
window = win32gui.GetWindowRect(hwnd)

start_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(window))
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    print('loop time {}'.format(time.time()-start_time))
    start_time = time.time()
