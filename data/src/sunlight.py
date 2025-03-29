from data.src.object import *  # 导入Object类

class Sunlight(Object):  # 定义Sunlight类，继承自Object类
    def __init__(self, screen, pos, type = 0):  # 初始化函数
        super().__init__(screen,
                         settings['sunlight']['path'],
                         settings['sunlight']['size'],
                         settings['sunlight']['imageCount']) # 调用父类的初始化函数
        self.type = type # 保存Sunlight类型
        self.pos = list(pos)  # 保存Sunlight位置
        self.posY = random.randint(GAME_SIZE[1] - 450, GAME_SIZE[1] - 60) # 随机生成Sunlight的Y坐标
        self.posNum = 0 # 位置变化标志
        self.preIndexTimeNumber = 0.05 # 初始化时间间隔
        self.time = 0 # 初始化时间
        self.delete = False # 删除标志
        self.posY_Ready = False # Y坐标准备标志
    
    def run(self):  # 运行函数
        self.update() # 更新函数
        if self.posY_Ready or self.type == 1:
            self.time += 1 # 增加时间
        if self.time > SUNLIGHT_DELETE_TIME: # 如果时间大于设定值
            self.delete = True # 设置删除标志
        if self.pos[1] < self.posY and self.type == 0 or self.posNum < 50: # 如果Y坐标小于设定值
            self.posNum += 1 # 增加位置
            self.pos[1] += 1 # 增加Y坐标
        else: # 否则
            if not self.posY_Ready:
                self.posY_Ready = True # 修改Y坐标准备标志
        self.draw()  # 绘制