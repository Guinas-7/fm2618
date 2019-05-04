import pygame, sys
from time import sleep
from pygame.locals import *
import random,math
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Billiards")

timer=0
collisiondelay = 500

FPS = 480
screenx = 1000
screeny = 800
screen = pygame.display.set_mode((screenx, screeny))

tabledimentions = (25,125,975,675)


ballradius = 25
balldrag = 0.0001


class ball:

    def __init__(self,x,y,color,angle, speed):
        self.radius = ballradius
        self.color = color
        self.xpos = x
        self.ypos = y
        self.angle = angle
        self.speed = speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.xpos), int(self.ypos)), self.radius,0)

    def move(self):
        self.xpos += self.speed*math.cos(math.radians(self.angle))
        self.ypos += self.speed*math.sin(math.radians(self.angle))

    def slowdown(self):
        if self.speed > 0:
            self.speed -= balldrag
        if self.speed<0:
            self.speed = 0

    def ballcolision(self,ball2):
        theta1 = math.radians(self.angle)
        theta2 = math.radians(balls[ball2].angle)
        phi = math.atan2((balls[ball2].ypos - self.ypos), (balls[ball2].xpos - self.xpos))

        v1 = self.speed
        v2 = balls[ball2].speed

        dx1F = v2 * math.cos(theta2 - phi) * math.cos(phi) - v1 * math.sin(theta1 - phi) * math.sin(phi)
        dy1F = v2 * math.cos(theta2 - phi) * math.sin(phi) + v1 * math.sin(theta1 - phi) * math.cos(phi)

        dx2F = v1 * math.cos(theta1 - phi) * math.cos(phi) - v2 * math.sin(theta2 - phi) * math.sin(phi)
        dy2F = v1 * math.cos(theta1 - phi) * math.sin(phi) + v2 * math.sin(theta2 - phi) * math.cos(phi)

        self.angle = math.degrees(math.atan2(dy1F, dx1F))
        balls[ball2].angle = math.degrees(math.atan2(dy2F, dx2F))

        self.speed = math.sqrt(math.pow(dx1F, 2) + math.pow(dy1F, 2))
        balls[ball2].speed = math.sqrt(math.pow(dx2F, 2) + math.pow(dy2F, 2))


class wall:
    def __init__(self, x, y, xlen, ylen, orientation):
        self.xpos = x
        self.ypos = y
        self.xlen = xlen
        self.ylen = ylen
        self.orientation = orientation
        self.color = (255,255,255)

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.xpos), int(self.ypos), int(self.xlen), int(self.ylen)))


balls = [ball(400,400,(255,255,255), 0,1),
         ball(700,400,(100,10,100), 10,0),
         ball(782,441,(100,10,100), 10,0),
         ball(782,359,(100,10,100), 10,0),
         ball(864,400,(100,10,100), 10,0),
         ball(864,483,(100,10,100), 10,0),
         ball(864,317,(100,10,100), 10,0)]

walls = [wall(0,100,1000,25,"horizontal"),
         wall(0,700,1000,25,"horizontal"),
         wall(0,100,25,600,"vertical"),
         wall(975,100,25,600,"vertical")]


def collisiondetect():
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if ((balls[i].xpos-balls[j].xpos)**2)+((balls[i].ypos-balls[j].ypos)**2) <= (balls[i].radius+balls[j].radius)**2:
                balls[i].ballcolision(j)

    return


while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    i = 0
    while i < len(balls):
        if balls[i].xpos-balls[i].radius <= tabledimentions[0] or balls[i].xpos+balls[i].radius >= tabledimentions[2]:
            balls[i].angle = math.degrees(math.pi - math.radians(balls[i].angle))
        if balls[i].ypos-balls[i].radius <= tabledimentions[1] or balls[i].ypos+balls[i].radius >= tabledimentions[3]:
            balls[i].angle = math.degrees(-math.radians(balls[i].angle))
        balls[i].draw()
        balls[i].move()
        balls[i].slowdown()
        i += 1

    i = 0
    while i < len(walls):
        walls[i].draw()
        i += 1

    collisiondetect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
