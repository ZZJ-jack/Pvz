from data.src.object import *

class gridPlant(Object):  # 定义plant类，继承自object类
    def __init__(self, screen):  # 初始化函数
        self.plantName = ""
        super().__init__(screen, '', (), 0)

    def updatePos(self):
        ifpos = getGridPos(pygame.mouse.get_pos())["if"]
        pos = getGridPos(pygame.mouse.get_pos())["pos"]
        if not ifpos:
            return
        pos[0] += settings['game']['gridPlantPos'][self.plantName][0]
        pos[1] += settings['game']['gridPlantPos'][self.plantName][1]
        self.pos = pos

    def run(self):  # 运行函数
        self.update()  # 更新图片
        self.updatePos()  # 更新位置
        self.draw()  # 绘制