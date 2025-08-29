from data.src.object import * # 导入对象
from data.src.pea import * # 导入豌豆

class Peashooter(Object):  # 定义Peashooter类，继承自Object类
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = 'peashooter'
        self.game = game
        super().__init__(game.screen, settings['peashooter']['path'], settings['peashooter']['size'], settings['peashooter']['imageCount'], self.plantType)  # 调用父类初始化函数
        self.pea_list = game.pea_list  # 豌豆列表
        self.pos = list(pos)  # 保存Peashooter位置
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.peaTime = 0
        self.ifAppendPea = False
        self.updateGrid(self.pos)
        self.grid[1] += 1

    def run(self):  # 运行函数
        self.update()  # 更新图片
        if self.animation: # 如果处于动画状态
            if self.peaTime < PEATIME:
                if self.game.zombiePos[self.grid[1]]: # 如果有僵尸
                    self.peaTime += 1
            elif self.peaTime == PEATIME:
                self.path = settings['peashooter']['path']  # 获取Peashooter图片路径
                self.imageCount = settings['peashooter']['imageCount']  # 获取Peashooter图片数量
                self.peaTime = 0
                self.ifAppendPea = False
        if self.peaTime == PEATIME:
            if self.path == settings['peashooter']['path']:
                self.path = settings['peashooter']['shoot_path']  # 获取Peashooter图片路径
                self.imageCount = settings['peashooter']['shoot_imageCount']  # 获取Peashooter图片数量
                self.imageIndex = 1
            if self.imageIndex == 6 and not self.ifAppendPea:
                self.pea_list.append(Pea((self.pos[0] + 35, self.pos[1] + 20), self.screen, self.grid[1]))
                self.ifAppendPea = True
        self.draw()  # 绘制图片