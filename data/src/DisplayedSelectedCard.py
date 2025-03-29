from data.src.object import *

class DisplayedSelectedCard(Object):  # 定义Card类，继承自object类
    def __init__(self, screen, name, PosNumber):  # 初始化函数
        super().__init__(screen,
                         settings['plant_card_path'][settings['plant_name'].index(name)],
                         CARD_SIZE,1)
        self.pos = [CARD_FIRST_X + (CARD_SIZE[0] + 7) * (PosNumber - 1),
                    CARD_POS_Y]
        self.name = name
        self.PosNumber = PosNumber
        self.number = settings['plant_name'].index(self.name)
        self.click = False
        self.clickTime = 0
        self.updata()  # 更新函数

    def run(self):  # 运行函数
        self.draw()  # 绘制
        if self.click:
            self.clickTime += 1
            if self.clickTime == 10:
                self.clickTime = 0
                self.click = False