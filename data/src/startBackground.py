from data.src.object import *

class StartBackground(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['startBackground']['path'], settings['startBackground']['size'], 1)
        self.pos = settings['startBackground']['pos']

    def run(self):
        self.updata()
        self.draw()