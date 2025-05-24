from data.src.object import *

class Plant(Object):  # 定义plant类，继承自object类
    def __init__(self, screen):  # 初始化函数
        self.name = ""
        super().__init__(screen, '', (), 0)

    def run(self):  # 运行函数
        self.update()  # 更新图片
        self.pos = list(pygame.mouse.get_pos())
        self.pos[0] += settings["game"]["mousePlantPos"][self.name][0]
        self.pos[1] += settings["game"]["mousePlantPos"][self.name][1]
        self.draw()  # 绘制