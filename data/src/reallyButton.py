from data.src.object import *

class ReallyButton(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['reallyButton']['path'], settings['reallyButton']['size'], 1)
        self.really = False
        self.reallyTime = 0
        self.start = False
        self.preStartTime = 0
        self.pos = settings['reallyButton']['pos']
        self.click = False

    def run(self):
        self.update()
        if self.click:
            self.reallyTime += 1
            if self.reallyTime > 5:
                self.really = False
            if self.reallyTime > 10:
                self.really = True
            if self.reallyTime > 15:
                self.really = False
            if self.reallyTime > 20:
                self.really = True
            if self.reallyTime > 25:
                self.really = False
                self.start = True
        if pygame.mouse.get_pressed()[0] and click(self.pos, self.size, pygame.mouse.get_pos()):
            self.really = True
            self.click = True
        if self.really:
            self.draw()