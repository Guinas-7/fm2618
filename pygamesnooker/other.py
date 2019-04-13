import pygame, sys
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("title of game")
shootdelay = 25
enemiespawn = 30
clockspeed = 60
screenx = 1000
screeny = 800
screen = pygame.display.set_mode((screenx, screeny))
bullets = []
enemies = []
enemie_image = pygame.image.load("spaceInv.png").convert_alpha()
enemiesizeX = 43
enemiesizeY = 34
playersizeX = 50
playersizeY = 50

player_image = pygame.image.load("spaceship.png").convert_alpha()



class bullet:

    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        self.radius = 4
        self.speed = 0

    def draw(self):
        pygame.draw.circle(screen, (100, 100, 100), (self.xpos, self.ypos), self.radius, 0)

    def move(self):
        if self.ypos > 0:
            self.ypos -= self.speed


class enemie:

    def __init__(self):
        self.xpos = -100
        self.ypos = 100
        self.speed = 4
        self.direction = 1

    def draw(self):
        screen.blit(enemie_image, (self.xpos, self.ypos))

    def move(self):
        if self.xpos < screenx:
            self.xpos += self.speed * self.direction

    def hit_by(self,raindrop):
        return ((self.xpos + enemiesizeX / 2)- raindrop.xpos)**2 +((self.ypos + enemiesizeY / 2)- raindrop.ypos)**2 < (enemiesizeX / 2)**2



class player:

    def __init__(self):
        self.xpos = 500
        self.ypos = 700

    def draw(self):
        screen.blit(player_image, (self.xpos, self.ypos))

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RIGHT]:
            self.xpos = self.xpos + 10
        if pressed_key[K_LEFT]:
            self.xpos = self.xpos - 10

    def shoot(self):
            newbullet = bullet(self.xpos + int(playersizeX/2), self.ypos + int(playersizeY/2))
            bullets.append(newbullet)




newplayer = player()

framecountershoot = shootdelay
framecounterenemie = enemiespawn
while True:
    screen.fill((0, 0, 0))
    newplayer.move()
    newplayer.draw()
    clock.tick(clockspeed)
    if framecountershoot <= 0:
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_SPACE]:
            newplayer.shoot()
            framecountershoot = shootdelay
    framecountershoot -= 1


    if framecounterenemie <= 0:
        newenemie = enemie()
        enemies.append(newenemie)
        framecounterenemie = enemiespawn
    framecounterenemie -= 1

    k = 0

    while k < len(enemies):
        enemies[k].draw()
        enemies[k].move()
        if enemies[k].xpos >= screenx - enemiesizeY/2 and enemies[k].direction == 1:
            enemies[k].direction = -1
            enemies[k].ypos += enemiesizeY + 30
        if enemies[k].xpos <= enemiesizeY / 2 and enemies[k].direction == -1:
            enemies[k].direction = 1
            enemies[k].ypos += enemiesizeY + 30
        i = 0
        while i < len(bullets) and k < len(enemies):
            if enemie.hit_by(enemies[k], bullets[i]):
                del bullets[i]
                del enemies[k]
                i -= 1
            i += 1
        k += 1

    i = 0
    while i < len(bullets):
        bullets[i].draw()
        bullets[i].move()
        if bullets[i].ypos <= 0:
            del bullets[i]
            i -= 1

        i += 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
