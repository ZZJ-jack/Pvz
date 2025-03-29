from data.src.object import *  # 导入对象

class Shovel(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['shovel']['path'], settings['shovel']['size'], 1)
        self.pos = settings['shovelFrame']['pos']
        self.use = False
        self.click = False
        self.clickTime = 0

    def run(self):
        if self.use:
            self.pos = pygame.mouse.get_pos()
            self.pos = list(self.pos)
            self.pos[1] -= 30
            self.pos[0] -= 30
        else:
            self.pos = settings['shovelFrame']['pos']
        if self.click:
            self.clickTime += 1
            if self.clickTime > 10:
                self.click = False
                self.clickTime = 0
        self.updata()
        self.draw()