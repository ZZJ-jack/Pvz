from data.src.object import *

class CardFrame(Object):  # 定义CardFrame类，继承自object
    def __init__(self, screen):  # 初始化函数
        super().__init__(screen, settings['cardframe']['path'], settings['cardframe']['size'], 1)
        self.pos = list(settings['cardframe']['pos'])  # 保存CardFrame位置
    def run(self):
        self.update()
        self.draw()