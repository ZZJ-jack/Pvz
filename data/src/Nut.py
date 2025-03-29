from data.src.object import * # 导入对象

class Nut(Object):  # 定义nut类，继承自Object类
    def __init__(self, screen, pos):  # 初始化函数
        self.plantType = 'nut'
        super().__init__(screen, settings['nut']['path1'], settings['nut']['size'], settings['nut']['imageCount1'], self.plantType)  # 调用父类初始化函数
        self.pos = list(pos)  # 保存nut位置
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.peaTime = 0
        self.ifAppendPea = False
        self.updataGrid(self.pos)
        self.grid[1] += 1

    def run(self):  # 运行函数
        self.update()  # 更新图片
        self.draw()  # 绘制图片