from data.src.object import *
from data.src.ZombieHead import *  # 导入僵尸头

class CherryBomb(Object):  # 定义CherryBomb类，继承自Object类
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = "cherry_bomb" # 设置植物类型为cherry_bomb
        self.game = game  # 保存游戏引用
        super().__init__(game.screen, settings[self.plantType]["initExplosionPath"], settings[self.plantType]["size"], settings[self.plantType]["initExplosionImageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]
        self.updateGrid(self.pos)
        self.grid[1] += 1
        self.state = "InitExplosion"
        self.delete = 0

    def run(self):  # 运行函数，用于更新樱桃炸弹的状态并绘制图片
        # 当樱桃炸弹处于初始爆炸状态且图片索引达到图片总数时
        if self.state == "InitExplosion" and self.imageIndex == self.imageCount:
            self.game.cherryBombExplosionMusic.play()  # 播放樱桃炸弹爆炸音效
            self.state = "Explosion"  # 切换状态为爆炸状态
            self.imageIndex = 0  # 重置图片索引为0
            self.path = settings[self.plantType]["ExplosionPath"]   # 更新图片路径为爆炸图片路径
            self.imageCount = settings[self.plantType]["ExplosionImageCount"] # 更新图片总数为爆炸图片总数
            self.size = settings[self.plantType]["ExplosionSize"] # 更新图片大小为爆炸图片大小
            self.pos[0] += settings[self.plantType]["ExplosionPosOffset"][0] # 调整位置以适应爆炸图片
            self.pos[1] += settings[self.plantType]["ExplosionPosOffset"][1] # 调整位置以适应爆炸图片
            self.updateGrid(self.pos)
            self.grid[1] += 1
            self.grid[0] += 1
            # 遍历游戏中的所有僵尸
            for zombie in self.game.zombie_list:
                if zombie.grid[1] != self.grid[1] and zombie.grid[1] != self.grid[1] - 1 and zombie.grid[1] != self.grid[1] + 1: # 当僵尸不在樱桃炸弹的爆炸范围内时
                    continue
                if self.grid[0] <= GRID_COUNT[0] - 1: # 当樱桃炸弹不在最后一列时
                    if zombie.grid[0] != self.grid[0] and zombie.grid[0] != self.grid[0] + 1 and zombie.grid[0] != self.grid[0] - 1: # 当僵尸的网格位置与樱桃炸弹的爆炸范围重合时
                        continue  
                else:  # 当樱桃炸弹在最后一列时
                    if not zombie.InRightVirtualGrid: # 如果僵尸在右侧虚拟网格内
                        continue
                # 当僵尸的网格位置与樱桃炸弹的爆炸范围重合时
                if zombie.hp > 40:  # 如果僵尸的生命值大于40
                    self.game.zombieHead_list.append(ZombieHead(self.game.screen, (zombie.pos[0] + 20, zombie.pos[1])))  # 在僵尸位置创建僵尸头
                zombie.hp = 0
                zombie.imageIndex = 0
                zombie.path = settings[zombie.type]["deadPath"]
                zombie.imageCount = settings[zombie.type]["deadImageCount"]
                flag = False
                # 初始化标志，用于判断该僵尸所在行是否还有其他僵尸
                for Zombie in self.game.zombie_list:
                    # 检查是否有僵尸与被吃僵尸在同一行
                    if zombie.posY == Zombie.posY:
                        # 若有，则将标志设为True并跳出循环
                        flag = True
                        break
                if not flag:
                    # 如果该行没有其他僵尸，更新游戏中该行的僵尸存在标志为False
                    self.game.zombiePos[zombie.posY] = False

        if self.state == "Explosion" and self.imageIndex == self.imageCount: # 当樱桃炸弹处于爆炸状态且图片索引达到图片总数时
            self.delete = True  # 标记为删除状态
        self.update()
        self.draw()