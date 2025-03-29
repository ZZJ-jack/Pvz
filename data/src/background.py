import pygame
from data.src.const import *
from data.src.settings import *
from data.src.object import *

# 定义背景类
class Background(Object):
    # 初始化背景类
    def __init__(self, screen):
        super().__init__(screen, settings['background']['path'], settings['background']['size'], 1)
        self.pos = list(settings['background']['pos'])
    def run(self):
        self.update()
        self.draw()