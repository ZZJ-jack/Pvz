from data.src.object import *

class ChooseCardFrame(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['ChooseCardFrame']['path'], settings['ChooseCardFrame']['size'], 1)
        self.updataImage()
        self.pos = settings['ChooseCardFrame']['pos']

    def run(self):
        self.draw()