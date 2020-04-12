import os

import cv2
import numpy as np
import win32gui
from PIL import ImageGrab
from pymouse import PyMouse


def equal(list1, list2):
    if list1[0] == list2[0] and list1[1] == list2[1] and list1[2] == list2[2]:
        return True
    else:
        return False


class MinesWeeper:
    def __init__(self):
        class_name = "TMain"
        title_name = "Minesweeper Arbiter "
        # 获取句柄
        hwnd = win32gui.FindWindow(class_name, title_name)
        # 获取窗口左上角和右下角坐标
        # left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        # print(left)
        self.window = win32gui.GetWindowRect(hwnd)
        self.ori_point = [self.window[0] + 15, self.window[1] + 101]
        self.area = [[-1 for i in range(16)] for j in range(30)]
        self.screen = cv2.cvtColor(np.array(ImageGrab.grab(self.window)), cv2.COLOR_BGR2RGB)
        self.screen_ori_point = [15, 101]

    def refresh_screen(self):
        self.screen = cv2.cvtColor(np.array(ImageGrab.grab(self.window)), cv2.COLOR_BGR2RGB)

    def get_block(self, locate: list):       # 获取[x,y]对应的方块(0,0)位置的色值
        return self.screen[self.ori_point[0] + 16 * (locate[0] - 1), self.ori_point[1] + 16 * (locate[1] - 1)]

    def click(self, locate: list, button=1):       # 点击[x,y]对应的方块 默认点击左键
        m = PyMouse()
        m.click(self.ori_point[0] + 16 * (locate[0] - 1), self.ori_point[1] + 16 * (locate[1] - 1), button=button)
