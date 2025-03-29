from data.src.object import *

class Card(Object):  # 定义Card类，继承自object类
    def __init__(self, screen, name, PosNumber):  # 初始化函数
        super().__init__(screen, settings['plant_card_path'][settings['plant_name'].index(name)], CARD_SIZE, 1)
        self.pos = [CARD_FIRST_X + (CARD_SIZE[0] + 7) * (PosNumber - 1), CARD_FIRST_Y] # 获取Card图片位置
        self.name = name
        self.number = PosNumber
        self.number = settings['plant_name'].index(self.name)
        self.READY = False

    def run(self):  # 运行函数
        self.update()
        if self.pos[1] < CARD_POS_Y:  # 如果Card图片位置在卡片位置之上
            self.pos[1] += 2  # 向下移动
        if self.pos[1] == CARD_POS_Y and not self.READY:
            self.READY = True
        self.draw()  # 绘制