from data.src.object import * # 导入对象

class Chomper(Object):  # 定义nut类，继承自Object类
    def __init__(self, screen, pos, zombie_list, zombie_head_list):  # 初始化函数
        self.plantType = "chomper"
        super().__init__(screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数
        self.pos = list(pos)  # 保存nut位置
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]
        self.updataGrid(self.pos)
        self.grid[1] += 1
        self.zombie_list = zombie_list  # 保存僵尸列表
        self.zombie_head_list = zombie_head_list  # 保存僵尸头列表
        self.state = "Idle" # 当前状态: 0: Idle, 1: Eat, 2: Eating

    def run(self):  # 运行函数
        self.update()  # 更新图片
        self.draw()  # 绘制图片