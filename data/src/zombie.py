from data.src.object import *

class Zombie(Object):  # 定义Zombie类，继承自object
    def __init__(self, game, type):  # 初始化函数，用于创建Zombie对象
        """
        初始化Zombie对象

        :param game: 游戏实例，包含游戏的各种信息和状态
        :param type: 僵尸类型，用于确定僵尸的属性
        """
        self.type = type  # 记录僵尸的类型
        # 调用父类Object的构造函数，初始化僵尸的屏幕、图片路径、尺寸和图片数量
        super().__init__(game, settings[self.type]["path"], settings[self.type]["size"], settings[self.type]["imageCount"])
        self.screen = game.screen  # 保存游戏屏幕对象，用于后续绘制操作
        self.game = game  # 保存游戏实例，方便访问游戏的其他信息
        self.eat = False  # 初始化僵尸是否在吃植物的状态，初始为False
        self.posY = random.randint(1, GRID_COUNT[1])  # 随机生成僵尸出现的行号，范围在1到GRID_COUNT[1]之间
        self.game.zombiePos[self.posY] = True  # 标记该行有僵尸出现
        self.pos = [ZONBIE_FIRST_X, GRID_Y[self.posY] - 25]  # 初始化僵尸的位置，X坐标为ZONBIE_FIRST_X，Y坐标根据随机生成的行号计算
        self.updateGrid(self.pos)  # 初始化grid属性
        self.hp = settings[self.type]["hp"]# 从配置文件中获取对应类型僵尸的初始生命值
        self.prePosTime = 0  # 记录上一次僵尸移动位置的时间，初始为0
        self.head = True  # 标记僵尸是否有头，初始为True
        self.delete = False  # 标记僵尸是否需要被删除，初始为False
        self.dieTime = 0  # 记录僵尸死亡后的持续时间，初始为0
        self.InRightVirtualGrid = 0  # 标记僵尸是否在右侧虚拟网格内，初始为False
        self.InGrid = False  # 标记僵尸是否在网格内，初始为False
        
    def run(self):  # 运行函数，用于更新僵尸的状态和绘制僵尸
        """
        运行函数，处理僵尸的状态更新和绘制操作
        """
        if self.hp <= 0:
            self.posY = -1  # 僵尸死亡后将其行号设为-1，表示不在任何行
            
        # 检查僵尸是否已死亡且处于死亡计时状态
        if self.dieTime != 0:
            # 死亡计时加1
            self.dieTime += 1
            # 若死亡计时达到60帧，标记僵尸为可删除状态并返回，不再执行后续逻辑
            if self.dieTime == 60:
                self.delete = True
                return
            # 绘制处于死亡状态的僵尸
            self.draw()  # 绘制
            return

        # 若僵尸尚未开始死亡计时
        if self.dieTime == 0:
            # 更新僵尸的状态
            self.update()  # 更新
            # 若僵尸生命值为0且动画标志为True
            if self.hp == 0 and self.animation:
                # 开始死亡计时
                self.dieTime += 1
                # 将图片索引设置为图片总数，可能显示最后一帧图片
                self.imageIndex = self.imageCount
                # 更新僵尸的图片显示
                self.updateImage()

        # 检查当前时间与上一次移动位置的时间间隔是否超过0.1秒，且僵尸生命值不为0
        if not time.time() - self.prePosTime <= 0.1 and self.hp != 0:  # 如果当前时间与上一次切换位置时间间隔不小于指定秒
            # 若僵尸正在吃植物且当前图片路径不是吃植物的图片路径
            if self.eat and not self.path == settings[self.type]["eatPath"]:
                # 将图片路径切换为吃植物的图片路径
                self.path = settings[self.type]["eatPath"]
                self.imageCount = settings[self.type]["eatImageCount"]
                # 重置图片索引为0
                self.imageIndex = 0
            # 若僵尸不在吃植物且当前图片路径是吃植物的图片路径
            elif not self.eat and self.path == settings[self.type]["eatPath"]:
                # 将图片路径切换为正常行走的图片路径
                self.path = settings[self.type]["path"]
                self.imageCount = settings[self.type]["imageCount"]
                # 重置图片索引为0
                self.imageIndex = 0
            # 更新上一次移动位置的时间
            self.prePosTime = time.time()  # 更新上一次切换位置时间
            # 若僵尸不在吃植物状态
            if not self.eat:  # 如果Zombie不在吃植物状态
                # 僵尸的X坐标减1，使其向左移动
                self.pos[0] -= 1

        # 根据僵尸当前位置更新其所在网格坐标
        self.updateGrid(self.pos)
        self.grid[0] += 1# 网格X坐标加1
        self.grid[1] += 1# 网格Y坐标加1
        self.InRightVirtualGrid = self.IsInRightVirtualGrid()  # 检查僵尸是否在右侧虚拟网格内
        self.InGrid = self.IsInGrid()  # 检查僵尸是否在网格内
        # 绘制僵尸
        self.draw()  # 绘制