from data.src.object import *

class GrowSoil(Object):  # 定义GrowSoil类，继承自object类
    def __init__(self, game, pos):  # 初始化函数
        self.name = ""
        self.game = game
        super().__init__(game.screen, settings["GrowSoil"]["path"], settings["GrowSoil"]["size"], settings["GrowSoil"]["imageCount"])
        self.pos = pos
        self.pos[0] += settings["GrowSoil"]["posChange"][0]
        self.pos[1] += settings["GrowSoil"]["posChange"][1]
        self.delete = False

    def run(self):  # 运行函数
        self.update()  # 更新图片
        if self.imageIndex >= self.imageCount:
            self.delete = True
        self.draw()  # 绘制