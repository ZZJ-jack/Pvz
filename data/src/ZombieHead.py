from data.src.object import *

class ZombieHead(Object):
    def __init__(self, screen, pos):
        super().__init__(screen, settings['zombie_head']['path'], settings['zombie_head']['size'], settings['zombie_head']['imageCount'])
        self.delete = False
        self.pos = pos
        self.Run = True
        self.deleteTime = 0
    
    def run(self):
        if self.Run:
            self.update()
            if self.animation:
                self.Run = False
                self.imageIndex = self.imageCount
                self.updataImage()
        else:
            self.deleteTime += 1
            if self.deleteTime == 60:
                self.delete = True
        self.draw()