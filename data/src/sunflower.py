from data.src.object import *
from data.src.sunlight import *

class Sunflower(Object):  # 定义Sunflower类，继承自Odject类
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = 'sunflower'
        self.game = game
        super().__init__(game.screen, settings['sunflower']['path'], settings['sunflower']['size'], settings['sunflower']['imageCount'], self.plantType)
        self.sunlight_list = game.sunlight_list
        self.pos = list(pos)  # 保存Sunflower位置
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.sunTime = 0
        self.ifAppendSun = False
        self.updateGrid(self.pos)
        self.grid[1] += 1

    def run(self):  # 运行函数
        self.update()  # 更新图片
        if self.animation:
            if self.sunTime < SUNTIME:
                self.sunTime += 1
            elif self.sunTime == SUNTIME:
                self.path = settings['sunflower']['path']  # 获取sunflower图片路径
                self.imageCount = settings['sunflower']['imageCount']  # 获取sunflower图片数量
                self.sunTime = 0
                self.ifAppendSun = False
        if self.sunTime == SUNTIME:
            if self.path == settings['sunflower']['path']:
                self.path = settings['sunflower']['shoot_path']  # 获取sunflower图片路径
                self.imageCount = settings['sunflower']['shoot_imageCount']  # 获取sunflower图片数量
                self.imageIndex = 1
            if self.imageIndex == 7 and not self.ifAppendSun:
                self.sunlight_list.append(Sunlight(self.screen, (self.pos[0] + 5, self.pos[1] - 25), 1))
                self.ifAppendSun = True
        self.draw()  # 绘制