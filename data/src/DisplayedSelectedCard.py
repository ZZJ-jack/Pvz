from data.src.object import *

class DisplayedSelectedCard(Object):  # 定义已选中卡片的显示类
    def __init__(self, screen, name, PosNumber):  # 初始化函数
        """
        初始化已选中的植物卡片，显示在游戏工具栏中
        参数:
            screen: 游戏屏幕对象，用于在该屏幕上绘制卡片
            name: 植物名称，用于标识卡片对应的植物
            PosNumber: 卡片在工具栏中的位置编号，用于确定卡片的显示位置
        """
        # 调用父类构造函数，加载卡片图片资源
        super().__init__(screen,
                         settings['plant_card_path'][settings['plant_name'].index(name)],
                         CARD_SIZE, 1)
        # 记录卡片在工具栏中的位置编号
        self.PosNumber = PosNumber
        # 记录卡片对应的植物名称
        self.name = name
        # 记录卡片在工具栏中的位置编号
        self.PosNumber = PosNumber
        # 获取卡片对应的植物编号
        self.number = settings['plant_name'].index(self.name)
        # 标记卡片是否被点击，初始状态为未点击
        self.click = False
        # 点击动画计时器，用于控制点击动画的持续时间
        self.clickTime = 0
        # 初始化图片资源
        self.update()

    def run(self):  # 每帧运行函数
        """处理卡片绘制和点击动画逻辑"""
        self.pos = [CARD_FIRST_X + (CARD_SIZE[0] + 7) * (self.PosNumber - 1),
                    CARD_POS_Y]
        self.draw()  # 绘制卡片到屏幕
        
        # 处理点击动画效果
        if self.click:
            self.clickTime += 1
            if self.clickTime == 10:  # 点击动画持续10帧
                self.clickTime = 0
                self.click = False