from data.src.object import *
from data.src.ZombieHead import *  # 导入僵尸头

class Jalapeno(Object):  # 定义火爆辣椒类，继承自Object类
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = "jalapeno" # 设置植物类型为火爆辣椒
        self.game = game  # 保存游戏引用
        super().__init__(game.screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]
        self.updateGrid(self.pos)
        self.grid[1] += 1
        self.oldGrid = self.grid.copy() # 记录旧的网格位置
        self.state = "InitExplosion"
        self.delete = 0

    def run(self):  # 运行函数，用于更新火爆辣椒的状态并绘制图片
        # 当火爆辣椒处于初始爆炸状态且图片索引达到图片总数时
        if self.state == "InitExplosion" and self.imageIndex == self.imageCount:
            self.game.jalapenoExplosionMusic.play()  # 播放火爆辣椒爆炸音效
            self.state = "Explosion"  # 切换状态为爆炸状态
            self.imageIndex = 1  # 重置图片索引为0
            self.path = settings[self.plantType]["ExplosionPath"]   # 更新图片路径为爆炸图片路径
            self.imageCount = settings[self.plantType]["ExplosionImageCount"] # 更新图片总数为爆炸图片总数
            self.size = settings[self.plantType]["ExplosionSize"] # 更新图片大小为爆炸图片大小
            self.updateImage()
            self.imageIndex = 0
            self.pos[0] = settings[self.plantType]["ExplosionPos"][0] # 调整位置以适应爆炸图片
            self.pos[1] += settings[self.plantType]["ExplosionPos"][1] # 调整位置以适应爆炸图片
            self.updateGrid(self.pos)
            self.grid[1] += 1
            self.grid[0] += 1
            # 遍历游戏中的所有僵尸
            for zombie in self.game.zombie_list:
                if zombie.grid[1] != self.grid[1]: # 当不在同一行时
                    continue
                if not zombie.InGrid: # 当不在网格内时
                    continue
                # 当僵尸的网格位置与火爆辣椒的爆炸范围重合时
                zombie.hp = 0
                zombie.imageIndex = 1
                zombie.path = settings["game"]["zombie-burn"]["Path"]  # 更新僵尸图片路径为燃烧状态图片路径
                zombie.imageCount = settings["game"]["zombie-burn"]["ImageCount"] # 更新僵尸图片总数为燃烧状态图片总数
                zombie.size = settings["game"]["zombie-burn"]["Size"] # 更新僵尸图片大小为燃烧状态图片大小
                zombie.pos[0] += settings["game"]["zombie-burn"]["Pos"][0] # 调整僵尸位置以适应燃烧状态图片
                zombie.pos[1] += settings["game"]["zombie-burn"]["Pos"][1] # 调整僵尸位置以适应燃烧状态图片
                zombie.state = "Burn"
                zombie.updateImage()
                zombie.imageIndex = 0
                self.game.zombiePos[zombie.posY] = False

        if self.state == "Explosion" and self.imageIndex == self.imageCount: # 当火爆辣椒处于爆炸状态且图片索引达到图片总数时
            self.delete = True  # 标记为删除状态
        self.update()
        self.draw()