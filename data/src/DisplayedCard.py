from data.src.object import *

class DisplayedCard(Object):  # 定义Card类，继承自object类
    def __init__(self, screen, name, ranks):  # 初始化函数
        super().__init__(screen,
                         settings['plant_card_path'][settings['plant_name'].index(name)],
                         CHOOSE_CARD_FRAME_CARD_SIZE,1)
        self.pos = (CHOOSE_CARD_FRAME_CARD_X[ranks[0]],
                    CHOOSE_CARD_FRAME_CARD_Y[ranks[1]])
        self.name = name
        self.number = settings['plant_name'].index(self.name)
        self.use = False

    def run(self):  # 运行函数
        self.updata()  # 更新函数
        self.draw()  # 绘制