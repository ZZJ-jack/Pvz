from data.src.object import *

class Shadow(Object):
    def __init__(self, screen, size, pos):
        super().__init__(screen, settings['shadow']['path'], size, 1)
        self.pos = pos
    
    def run(self):
        self.updata()
        self.draw()