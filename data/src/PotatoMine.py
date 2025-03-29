from data.src.object import * # 导入对象

class PotatoMine(Object):  # 定义PotatoMine类，继承自Object类
    def __init__(self, screen, pos):  # 初始化函数
        self.plantType = 'potato_mine'
        super().__init__(screen, settings['potato_mine']['initPath'], settings['potato_mine']['size'], settings['potato_mine']['initImageCount'], self.plantType)  # 调用父类初始化函数
        self.pos = list(pos)  # 保存PotatoMine位置
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.Explode = False
        self.grow = False
        self.growTime = 0
        self.updataGrid(self.pos)
        self.ExplodeTime = 0
        self.delete = False

    def run(self):  # 运行函数
        self.updata()  # 更新图片
        if self.Explode and self.ExplodeTime == 0:  # 如果PotatoMine爆炸
            self.path = settings['potato_mine']['explodePath']  # 更新图片路径
            self.imageIndex = 0
            self.imageCount = settings['potato_mine']['explodeImageCount']
            self.updata()  # 更新图片
            self.ExplodeTime += 1  # 增加爆炸时间

        elif self.Explode:  # 如果PotatoMine已经爆炸
            self.ExplodeTime += 1  # 增加爆炸时间
            if self.ExplodeTime >= settings['potato_mine']['explodeTime']:  # 如果爆炸时间达到设定值
                self.delete = True  # 销毁PotatoMine

        if not self.grow:  # 如果PotatoMine没有生长
            self.growTime += 1  # 增加生长时间
            if self.growTime >= settings['potato_mine']['growTime']:  # 如果生长时间达到设定值
                self.grow = True  # 设置为已经生长
                self.path = settings['potato_mine']['path']  # 更新图片路径
                self.imageIndex = 0
                self.imageCount = settings['potato_mine']['imageCount']
                self.updata()  # 更新图片
        
        self.draw()  # 绘制图片