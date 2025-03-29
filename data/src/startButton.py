from data.src.object import *

class StartButton(Object):
    def __init__(self, screen):
        super().__init__(screen, settings['startButton']['path'], settings['startButton']['size'], 1)
        self.start = False
        self.startTime = False
        self.Time = 0
        self.preStartTime = 0
        self.pos = settings['startButton']['pos']

    def run(self):
        self.update()
        if pygame.mouse.get_pressed()[0] and click(self.pos, self.size, pygame.mouse.get_pos()):
            self.startTime = True
        if self.startTime:
            self.Time += 1
            if self.Time == 5:
                self.Time = 0
                if self.path == settings['startButton']['onPath']:
                    self.path = settings['startButton']['path']
                    self.preStartTime += 1
                else:
                    self.path = settings['startButton']['onPath']
                if self.preStartTime == 3:
                    self.start = True
                    self.startTime = False
                    self.path = settings['startButton']['path']
        self.draw()