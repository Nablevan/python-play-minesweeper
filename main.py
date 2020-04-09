import numpy as np
import win32gui
from PIL import ImageGrab


class_name = "TMain"
title_name = "Minesweeper Arbiter "
# 获取句柄
hwnd = win32gui.FindWindow(class_name, title_name)
# 获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left)

