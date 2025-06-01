from data.src.object import *

class DisplayedCard(Object):  # 定义Card类，继承自object类
    def __init__(self, screen, name, ranks):
        """
        初始化显示在选择卡片界面的植物卡片
        
        参数:
            screen: 游戏屏幕对象，用于在该屏幕上绘制卡片
            name: 植物名称，用于标识卡片对应的植物
            ranks: 一个元组，包含卡片在选择卡片框中的行列位置，用于确定卡片的显示位置
        """
        # 调用父类的构造函数，加载卡片图片资源
        super().__init__(
                            screen,
                            settings['plant_card_path'][settings['plant_name'].index(name)],
                            CHOOSE_CARD_FRAME_CARD_SIZE,
                            1,
                        )
        # 根据行列位置计算卡片在屏幕上的坐标
        self.pos = (CHOOSE_CARD_FRAME_CARD_X[ranks[0]],
                    CHOOSE_CARD_FRAME_CARD_Y[ranks[1]])
        # 记录卡片对应的植物名称
        self.name = name
        # 获取卡片对应的植物编号
        self.number = settings['plant_name'].index(self.name)
        # 标记卡片是否被使用，初始状态为未使用
        self.use = False

    def run(self):  # 运行函数
        self.update()  # 更新函数
        self.draw()  # 绘制