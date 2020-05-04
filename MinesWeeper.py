import os
import time

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


dict_num = {(192, 192, 192): 0,
            (0, 0, 255): 1,
            (0, 128, 0): 2,
            (255, 0, 0): 3,
            (0, 0, 128): 4,
            (128, 0, 0): 5,
            (0, 128, 128): 6}


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
        self.screen_transpose = np.transpose(self.screen, (1, 0, 2))
        self.screen_ori_point = [15, 101]

    def refresh_screen(self):
        self.screen = cv2.cvtColor(np.array(ImageGrab.grab(self.window)), cv2.COLOR_BGR2RGB)

    def refresh_area(self):
        self.refresh_screen()
        for x in range(1, 31):
            for y in range(1, 17):
                self.area[x-1][y-1] = self.get_num([x, y])   # TODO 确认扫描出的位置和色值
                # self.click([x, y], 2)
                # time.sleep(2)

    def get_block(self, locate: list):  # 获取[x,y]对应的方块(0,0)位置的色值
        # locate.reverse()
        # color = self.screen[self.ori_point[0] + 16 * (locate[0] - 1), self.ori_point[1] + 16 * (locate[1] - 1)]
        color = self.screen_transpose[self.screen_ori_point[0] + 16 * (locate[0] - 1)][self.screen_ori_point[1] + 16 * (locate[1] - 1)]
        return list(color)

    def get_num(self, locate: list):  # 获取[x,y]对应的方块的雷数
        color = tuple(self.get_block(locate))
        return dict_num.get(color)

    def click(self, locate: list, button=1):  # 点击[x,y]对应的方块 默认点击左键
        m = PyMouse()
        m.click(self.ori_point[0] + 16 * (locate[0] - 1), self.ori_point[1] + 16 * (locate[1] - 1), button=button)


if __name__ == '__main__':
    a = MinesWeeper()
    # while True:
    #     cv2.imshow('window', a.screen)
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         cv2.destroyAllWindows()
    #         break
    # m = PyMouse()
    # m.click(161, 119, button=1)
    a.refresh_area()
    print('done')
