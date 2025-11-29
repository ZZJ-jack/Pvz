from data.src.object import *

class Lawnmower(Object):  # 定义Lawnmower类，继承自object类
    def __init__(self, screen, gridY):  # 初始化函数
        super().__init__(screen, settings['lawnmower']['path'], settings['lawnmower']['size'], settings['lawnmower']['imageCount'])
        self.gridY = gridY
        self.pos = [LAWNMOWER_FIRST_X, GRID_Y[gridY]]
        self.name = "lawnmower"
        self.GoOut = 0
        self.Delete = 0
        self.updateGrid(self.pos)
        self.grid[1] += 1

    def run(self):  # 运行函数
        if self.pos[0] < LAWNMOWER_POS_X:  # 如果Card图片位置在卡片位置之上
            self.pos[0] += 1  # 向右移动
            self.update()
        if self.GoOut == 1:
            self.pos[0] += 1
            if self.pos[0] >= GAME_SIZE[0]:
                self.Delete = 1
            self.update()
        self.draw()  # 绘制