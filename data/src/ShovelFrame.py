from data.src.object import *  # 导入对象

class ShovelFrame(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['shovelFrame']['path'], settings['shovelFrame']['size'], 1)
        self.pos = settings['shovelFrame']['pos']
    def run(self):
        self.updata()
        self.draw()