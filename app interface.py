import pygame
from pygame.locals import *
import sys
bg = (0,0,0)


class Meter:
    def __init__(self, screen, x = 100, y = 50, tightness = 100):
        self.x = x
        self.y = y
        self.tightness = tightness
        self.screen = screen
        self.meterrect = pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 100, tightness))
    def draw(self,tigtness):
        self.tightness=tigtness
        self.meterrect = pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, 100, self.tightness))





def main():
    pygame.init()
    screen = pygame.display.set_mode((480,720))
    screen.fill(bg)
    meter = Meter(screen)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
        meter.draw(500)
        pygame.display.update()




myImage = image.open('+ - sign.jpg')
myIamge.show()

main()