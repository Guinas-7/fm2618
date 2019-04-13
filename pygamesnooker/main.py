import pygame, sys
from pygame.locals import *
import random, math
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Billiards")

FPS = 120
screenx = 1000
screeny = 800
screen = pygame.display.set_mode((screenx, screeny))


ballradius = 50


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
            self.ypos -= self.speed*math.sin(math.radians(self.angle))


balls = [ball(200,200,(10,100,100),50,4),ball(600,200,(100,10,100), 45,3)]


def BallsCollide(ball1,ball2):
    theta1 = math.radians(balls[ball1].angle)
    #print(math.degrees(theta1))
    theta2 = math.radians(balls[ball2].angle)
    #print(math.degrees(theta2))
    phi = math.atan2((math.fabs(balls[ball2].ypos - balls[ball1].ypos)), math.fabs(balls[ball2].xpos - balls[ball1].xpos))


    print("impact angle: "+str(math.degrees(phi)))
    v1 = balls[ball1].speed
    v2 = balls[ball2].speed
    if v1 == 0:
        balls[ball2].angle = math.degrees(math.atan2(math.sin(phi) , (1 + math.cos(phi))))
        balls[ball1].angle = math.degrees((math.pi - phi) / 2)
        balls[ball2].speed = math.fabs(v1 * (math.sqrt(math.cos(phi))))
        balls[ball1].speed = math.fabs(v1 * math.sin(phi / 2))
        return
    if v2 == 0:
        balls[ball1].angle = math.degrees(math.atan2(math.sin(phi),(1+math.cos(phi))))
        balls[ball2].angle = math.degrees((math.pi-phi) / 2)
        balls[ball1].speed = math.fabs(v1*(math.sqrt(math.cos(phi))))
        balls[ball2].speed = math.fabs(v1*math.sin(phi/2))
        return

    dx1F = v2 * math.cos(theta2 - phi) * math.cos(phi) - v1 * math.sin(theta1 - phi) * math.sin(phi)
    dy1F = v2 * math.cos(theta2 - phi) * math.sin(phi) + v1 * math.sin(theta1 - phi) * math.cos(phi)
    print("dx1: " + str(dx1F))
    print("dy1: " + str(dy1F))
    dx2F = v1 * math.cos(theta1 - phi) * math.cos(phi) - v2 * math.sin(theta2 - phi) * math.sin(phi)
    dy2F = v1 * math.cos(theta1 - phi) * math.sin(phi) + v2 * math.sin(theta2 - phi) * math.cos(phi)
    print("dx2: " + str(dx2F))
    print("dx2: " + str(dy2F))

    if dx1F < 0:
        balls[ball1].angle = math.degrees(math.atan(dy1F/dx1F)) + 180
    else:
        balls[ball1].angle = math.degrees(math.atan(dy1F/dx1F))
    if dx2F < 0:
        balls[ball2].angle = math.degrees(math.atan(dy2F/dx2F)) + 180
    else:
        balls[ball2].angle = math.degrees(math.atan(dy2F/dx2F))

    balls[ball1].speed = math.sqrt(math.pow(dx1F,2) + math.pow(dy1F,2))
    balls[ball2].speed = math.sqrt(math.pow(dx2F,2) + math.pow(dy2F,2))

def CollisionDetect():
    for ball1 in balls:
        for ball2 in balls:
            if ball1 != ball2:
                if ((ball1.xpos-ball2.xpos)**2)+((ball1.ypos-ball2.ypos)**2) <= (ball1.radius+ball2.radius)**2:
                    print("initial ball 1 angle: " + str(balls[balls.index(ball1)].angle))
                    print("initial ball 1 speed: " + str(balls[balls.index(ball1)].speed))
                    print("initial ball 2 angle: " + str(balls[balls.index(ball2)].angle))
                    print("initial ball 2 speed: " + str(balls[balls.index(ball2)].speed))
                    print("colision")
                    BallsCollide(balls.index(ball1),balls.index(ball2))
                    print("final ball 1 angle: " + str(balls[balls.index(ball1)].angle))
                    print("final ball 1 speed: " + str(balls[balls.index(ball1)].speed))
                    print("final ball 2 angle: " + str(balls[balls.index(ball2)].angle))
                    print("final ball 2 speed: " + str(balls[balls.index(ball2)].speed))

                    return

while True:
    screen.fill((0, 0, 0))

    i = 0
    while i < len(balls):
        if balls[i].xpos-balls[i].radius <= 0 or balls[i].xpos+balls[i].radius >= screenx:
            balls[i].angle = math.degrees(math.pi - math.radians(balls[i].angle))
            print ("wallhit")
        if balls[i].ypos-balls[i].radius <= 0 or balls[i].ypos+balls[i].radius >= screeny:
            balls[i].angle = math.degrees(-math.radians(balls[i].angle))
            print("wallhit")
        balls[i].draw()
        balls[i].move()
        i += 1
    CollisionDetect()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()