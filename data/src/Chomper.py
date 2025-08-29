from data.src.object import * # 导入对象
from data.src.ZombieHead import * # 导入僵尸头


class Chomper(Object):  # 定义nut类，继承自Object类
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = "chomper"  # 设置植物类型为chomper
        self.game = game  # 保存游戏引用
        super().__init__(game.screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)  # 将传入的位置转换为列表并保存
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]  # 调整x坐标位置
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]  # 调整y坐标位置
        self.updateGrid(self.pos)  # 更新网格位置
        self.grid[1] += 1  # 调整网格y坐标
        self.state = "Idle" # 设置初始状态为Idle（空闲）
        self.eat = False # 设置初始状态为False（未进食）
        self.eattingTime = 0 # 设置进食时间为0

    def run(self):  # 运行函数，用于更新大嘴花的状态并绘制图片
        # 当大嘴花处于进食状态且图片索引为7时
        if self.state == "Eat" and self.imageIndex == 7:
            # 在游戏的僵尸头列表中添加一个新的僵尸头对象，位置在被吃僵尸位置基础上偏移
            self.game.zombieHead_list.append(ZombieHead(self.screen, (self.zombie.pos[0] + 20, self.zombie.pos[1])))
            # 检查被吃的僵尸是否在游戏的僵尸列表中
            if self.zombie in self.game.zombie_list:
                # 若存在，则从僵尸列表中移除该僵尸
                self.game.zombie_list.remove(self.zombie)
                # 初始化标志，用于判断该僵尸所在行是否还有其他僵尸
                flag = False
                # 遍历游戏中的所有僵尸
                for Zombie in self.game.zombie_list:
                    # 检查是否有僵尸与被吃僵尸在同一行
                    if self.zombie.posY == Zombie.posY:
                        # 若有，则将标志设为True并跳出循环
                        flag = True
                        break
                # 如果该行没有其他僵尸
                if not flag:
                    # 更新游戏中该行的僵尸存在标志为False
                    self.game.zombiePos[self.zombie.posY] = False
        # 当大嘴花处于进食状态且图片索引达到图片总数时
        elif self.state == "Eat" and self.imageIndex == self.imageCount:
            # 设置图片数量为持续进食状态的图片数量
            self.imageCount = settings[self.plantType]["eatingImageCount"]
            # 设置图片路径为持续进食状态的图片路径
            self.path = settings[self.plantType]["eatingPath"]
            # 重置图片索引为0
            self.imageIndex = 0
            # 设置状态为持续进食状态
            self.state = "Eating"
        # 当大嘴花处于持续进食状态时
        elif self.state == "Eating":
            # 进食时间加1
            self.eattingTime += 1
            # 检查进食时间是否达到预设的进食时长
            if self.eattingTime == settings[self.plantType]["eatingTime"]:
                # 若达到，则重置进食时间为0
                self.eattingTime = 0
                # 设置状态为空闲状态
                self.state = "Idle"
                # 设置图片数量为空闲状态的图片数量
                self.imageCount = settings[self.plantType]["imageCount"]
                # 设置图片路径为空闲状态的图片路径
                self.path = settings[self.plantType]["path"]
                # 设置进食状态为未进食
                self.eat = False

        # 调用更新方法，更新图片显示
        self.update()
        # 调用绘制方法，绘制大嘴花图片
        self.draw()

    def ToEat(self, zombie): # 定义ToEat函数
        self.zombie = zombie  # 保存被吃掉的僵尸引用
        self.imageCount = settings[self.plantType]["eatImageCount"]  # 设置图片数量为进食图片数量
        self.path = settings[self.plantType]["eatPath"]  # 设置图片路径为进食图片路径
        self.imageIndex = 0  # 重置图片索引为0
        self.state = "Eat"  # 设置状态为Eat（进食