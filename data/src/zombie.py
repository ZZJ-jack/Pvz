from data.src.object import *

class Zombie(Object):  # 定义Zombie类，继承自object
    def __init__(self, game, type):  # 初始化函数
        self.type = type
        super().__init__(game.screen, settings[self.type]["path"], settings[self.type]["size"], settings[self.type]["imageCount"])
        self.screen = game.screen  # 保存屏幕
        self.game = game  # 保存游戏
        self.eat = False  # 初始化Zombie是否在吃植物状态
        self.posY = random.randint(1, GRID_COUNT[1])
        self.game.zombiePos[self.posY] = True
        self.pos = [ZONBIE_FIRST_X, GRID_Y[self.posY] - 25]
        self.hp = settings[self.type]["hp"]  # 初始化Zombie血量
        self.prePosTime = 0
        self.head = True
        self.delete = False
        self.dieTime = 0
    def run(self):  # 运行函数
        if self.dieTime != 0:
            self.dieTime += 1
            if self.dieTime == 60:
                self.delete = True
                return
            self.draw()  # 绘制
            return
        if self.dieTime == 0:
            self.update()  # 更新
            if self.hp == 0 and self.animation:
                self.dieTime += 1
                self.imageIndex = self.imageCount
                self.updataImage()
        if not time.time() - self.prePosTime <= 0.1 and self.hp != 0:  # 如果当前时间与上一次切换位置时间间隔不小于指定秒
            if self.eat and not self.path == settings[self.type]["eatPath"]:
                self.path = settings[self.type]["eatPath"]
            elif not self.eat and self.path == settings[self.type]["eatPath"]:
                self.path = settings[self.type]["path"]
            self.prePosTime = time.time()  # 更新上一次切换位置时间
            if not self.eat:  # 如果Zombie不在吃植物状态
                self.pos[0] -= 1
        self.updataGrid(self.pos)
        self.grid[0] += 1
        self.grid[1] += 1
        self.draw()  # 绘制