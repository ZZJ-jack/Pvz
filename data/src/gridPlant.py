from data.src.object import *

class gridPlant(Object):  # 定义plant类，继承自object类
    def __init__(self, screen):  # 初始化函数
        self.plantType = ''
        super().__init__(screen, '', (), 0)

    def run(self):  # 运行函数
        self.update()  # 更新图片
        pos = getGridPos(list(pygame.mouse.get_pos()))
        if not pos:
            return
        self.pos = pos
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.draw()  # 绘制