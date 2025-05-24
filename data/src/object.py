import pygame
import time
import random
import math
from data.src.const import *  # 导入常量
from data.src.settings import *  # 导入设置
from data.src.tools import *  # 导入工具函数

class Object(pygame.sprite.Sprite):  # 定义基类
    def __init__(self, screen, path, size, imageCount, plantType = 'not plant'):  # 初始化函数
        self.screen = screen  # 保存屏幕
        self.pos = [0, 0]
        self.path = path
        self.size = size
        self.imageCount = imageCount  # 获取图片数量
        self.imageIndex = 0  # 初始化图片索引
        self.preIndexTime = 0  # 初始化切换角色时间
        self.hp = 100
        self.hpTime = 0
        self.animation = False
        if plantType == 'not plant':
            self.preIndexTimeNumber = 0.1
        else:
            self.preIndexTimeNumber = settings['game']['plantPreIndexTimeNumber'][plantType]
    
    def updataImage(self):  # 更新图片函数
        if self.imageCount == 1:  # 获取当前图片路径
            path = self.path
        else:
            path = self.path % self.imageIndex
        self.image = pygame.image.load(path)  # 加载图片
        self.image = pygame.transform.scale(self.image, self.size)  # 缩放图片
    
    def getRect(self):  # 获取图片矩形函数
        rect = self.image.get_rect()  # 获取图片矩形
        rect.x, rect.y = self.pos  # 设置矩形位置
        return rect
    
    def update(self):  # 更新函数
        if self.imageCount != 1:
            if time.time() - self.preIndexTime <= self.preIndexTimeNumber:  # 如果当前时间与上一次切换角色时间间隔小于指定秒
                return  # 不更新图片
            self.preIndexTime = time.time()  # 更新上一次切换角色时间
            self.imageIndex = (self.imageIndex + 1) % self.imageCount  # 更新图片索引
            if self.imageIndex == 0:  # 如果图片索引为0
                self.animation = True  # 设置动画为True
                self.imageIndex = 1  # 设置图片索引为1

        self.updataImage()  # 更新图片
    
    def updataGrid(self, pos):
        self.grid = getGrid(pos)

    def draw(self):  # 绘制函数
        self.screen.blit(self.image, self.getRect())  # 将图片绘制到屏幕上
        if self.animation:
            self.animation = False