from data.src.object import * # 导入对象
from data.src.ZombieHead import * # 导入僵尸头


class Chomper(Object):  # 定义nut类，继承自Object类
    def __init__(self, screen, pos, zombie_list, zombie_head_list):  # 初始化函数
        self.plantType = "chomper"  # 设置植物类型为chomper
        super().__init__(screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)  # 将传入的位置转换为列表并保存
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]  # 调整x坐标位置
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]  # 调整y坐标位置
        self.updataGrid(self.pos)  # 更新网格位置
        self.grid[1] += 1  # 调整网格y坐标
        self.zombie_list = zombie_list  # 保存僵尸列表引用
        self.zombie_head_list = zombie_head_list  # 保存僵尸头列表引用
        self.state = "Idle" # 设置初始状态为Idle（空闲）
        self.eat = False # 设置初始状态为False（未进食）
        self.eattingTime = 0 # 设置进食时间为0

    def run(self):  # 运行函数

        if self.state == "Eat" and self.imageIndex == 7:
            self.zombie_head_list.append(ZombieHead(self.screen, (self.zombie.pos[0] + 20, self.zombie.pos[1])))  # 添加僵尸头对象
            if self.zombie in self.zombie_list:  # 如果僵尸在僵尸列表中
                self.zombie_list.remove(self.zombie)  # 移除被吃掉的僵尸
        elif self.state == "Eat" and self.imageIndex == self.imageCount:  # 如果状态为Eat（进食）
            self.imageCount = settings[self.plantType]["eatingImageCount"]  # 设置图片数量为进食图片数量
            self.path = settings[self.plantType]["eatingPath"]  # 设置图片路径为进食图片路径
            self.imageIndex = 0  # 重置图片索引为0
            self.state = "Eating"  # 设置状态为Eat（进食）
        elif self.state == "Eating":
            self.eattingTime += 1 # 进食时间加1
            if self.eattingTime == settings[self.plantType]["eatingTime"]: # 如果进食时间为10
                self.eattingTime = 0 # 重置进食时间
                self.state = "Idle" # 设置状态为Idle（空闲）
                self.imageCount = settings[self.plantType]["imageCount"] # 设置图片数量为空闲图片数量
                self.path = settings[self.plantType]["path"] # 设置图片路径为空闲图片路径
                self.eat = False # 设置状态为False（未进食）

        self.update()  # 更新图片
        self.draw()  # 绘制图片

    def ToEat(self, zombie): # 定义ToEat函数
        self.zombie = zombie  # 保存被吃掉的僵尸引用
        self.imageCount = settings[self.plantType]["eatImageCount"]  # 设置图片数量为进食图片数量
        self.path = settings[self.plantType]["eatPath"]  # 设置图片路径为进食图片路径
        self.imageIndex = 0  # 重置图片索引为0
        self.state = "Eat"  # 设置状态为Eat（进食