import pygame
from pygame.locals import *
import sys
bg = (0,0,0)

meterheight = 500

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


class Button:
    x = 0
    y = 0
    image = 0
    def __init__(self):
        pass

    def draw(self, imagefile, x, y, gameDisplay):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imagefile)
        gameDisplay.blit(self.image,(self.x, self.y))


    def check_mouse(self,pos,click,direction):
        mx = pos[0]
        my = pos[1] #this was set to pos[0] I changed it to pos[1]  now it works - Mr Aronson
        global meterheight

        #print(pos)
        if self.x < mx and self.x + 180 > mx and self.y < my and self.y + 180 > my and click:
            print("click", direction)
            if direction == "up":
                meterheight = meterheight + 100
            else:
                meterheight = meterheight - 100

def main():
    pygame.init()
    screen = pygame.display.set_mode((480,720))

    meter = Meter(screen)
    plusbutton = Button()
    minusbutton = Button()
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        pos = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()
        screen.fill(bg)
        #print(meterheight)
        meter.draw(meterheight)
        plusbutton.draw("plus.png",300,100,screen)
        minusbutton.draw("minus.png",300,300,screen)
        plusbutton.check_mouse(pos, click, "up")
        minusbutton.check_mouse(pos, click, "down")

        pygame.display.update()


main()