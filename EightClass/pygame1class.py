import pygame, sys
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("title of game")
clouddelay = 500
clockspeed = 60
screenx = 1000
screeny = 800
screen = pygame.display.set_mode((screenx, screeny))
drops = []
clouds = []
cloud_image = pygame.image.load("cloud.png").convert_alpha()
figure_image = pygame.image.load("figure.png").convert_alpha()



class drop:

    def __init__(self,xmin,xmax,y):
        self.xpos = random.randint(xmin,xmax)
        self.ypos = y
        self.randradius = random.randint(1,3)
        self.speed = random.randint(3,6)

    def draw(self):
        pygame.draw.circle(screen, (100, 100, 100), (self.xpos, self.ypos), self.randradius, 0)

    def move(self):
        if self.ypos < screeny:
            self.ypos += self.speed


class cloud:

    def __init__(self):
        self.xpos = -500
        self.ypos = random.randint(0,40)
        self.speed = 1

    def draw(self):
        screen.blit(cloud_image, (self.xpos, self.ypos))

    def move(self):
        if self.xpos < screenx:
            self.xpos += self.speed

    def rain(self):
        newdrop = drop(self.xpos + 50,self.xpos+435,self.ypos+150)
        drops.append(newdrop)

class figure:

    def __init__(self):
        self.xpos = 500
        self.ypos = 600

    def draw(self):
        screen.blit(figure_image, (self.xpos, self.ypos))

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RIGHT]:
            self.xpos = self.xpos + 10
        if pressed_key[K_LEFT]:
            self.xpos = self.xpos - 10

    def hit_by(self,raindrop):
        return ((self.xpos + 93)- raindrop.xpos)**2 +((self.ypos + 93)- raindrop.ypos)**2 < 8649



newfigure = figure()

newcloud = cloud()
clouds.append(newcloud)
framecounter = clouddelay
while True:
    screen.fill((0, 0, 0))
    newfigure.move()
    newfigure.draw()
    clock.tick(clockspeed)
    if framecounter <= 0:
        newcloud = cloud()
        clouds.append(newcloud)
        framecounter = clouddelay
    framecounter -= 1

    k = 0
    while k < len(clouds):
        clouds[k].draw()
        clouds[k].move()
        clouds[k].rain()
        if clouds[k].xpos >= screenx:
            del clouds[k]
            k -= 1
        k += 1

    i = 0
    while i < len(drops):
        drops[i].draw()
        drops[i].move()
        if drops[i].ypos >= screeny:
            del drops[i]
            i -= 1
        if figure.hit_by(newfigure,drops[i]):
            del drops[i]
            i -= 1
        i += 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
