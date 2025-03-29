from data.src.object import *

class DisplayedSelectedCard(Object):  # 定义已选中卡片的显示类
    def __init__(self, screen, name, PosNumber):  # 初始化函数
        """
        初始化已选中的植物卡片
        参数：
            screen: 游戏屏幕对象
            name: 植物名称 
            PosNumber: 卡片在工具栏中的位置编号
        """
        # 调用父类构造函数，加载卡片图片资源
        super().__init__(screen,
                         settings['plant_card_path'][settings['plant_name'].index(name)],
                         CARD_SIZE, 1)
        # 设置卡片位置（基于工具栏布局计算）
        self.pos = [CARD_FIRST_X + (CARD_SIZE[0] + 7) * (PosNumber - 1),
                    CARD_POS_Y]
        self.name = name            # 植物名称
        self.PosNumber = PosNumber  # 位置编号
        self.number = settings['plant_name'].index(self.name)  # 获取植物编号
        self.click = False    # 点击状态标记
        self.clickTime = 0    # 点击动画计时器
        self.update()         # 初始化图片资源

    def run(self):  # 每帧运行函数
        """处理卡片绘制和点击动画逻辑"""
        self.draw()  # 绘制卡片到屏幕
        
        # 处理点击动画效果
        if self.click:
            self.clickTime += 1
            if self.clickTime == 10:  # 点击动画持续10帧
                self.clickTime = 0
                self.click = False