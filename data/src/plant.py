from data.src.object import *

class Plant(Object):  # 定义plant类，继承自object类
    def __init__(self, screen):  # 初始化函数
        super().__init__(screen, '', (), 0)

    def run(self):  # 运行函数
        self.updata()  # 更新图片
        self.pos = list(pygame.mouse.get_pos())
        self.pos[0] -= 30
        self.pos[1] -= 30
        self.draw()  # 绘制