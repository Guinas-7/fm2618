import pygame, sys
from time import sleep
from pygame.locals import *
import random,math
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Billiards")

timer=0
collisiondelay = 500

FPS = 240
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
        self.ypos += self.speed*math.sin(math.radians(self.angle))


balls = [ball(200,600,(10,100,100),58,5),ball(800,500,(100,10,100), 17,3),ball(700,100,(100,10,100), 17,3),ball(900,600,(100,10,100), 17,3),ball(800,300,(100,10,100), 17,3)]


def BallsCollide(ball1,ball2):
    theta1 = math.radians(balls[ball1].angle)
    theta2 = math.radians(balls[ball2].angle)
    phi = math.atan2((balls[ball2].ypos - balls[ball1].ypos), (balls[ball2].xpos - balls[ball1].xpos))

    print(str(math.degrees(phi)) + "        impact angle: ")
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

    dx2F = v1 * math.cos(theta1 - phi) * math.cos(phi) - v2 * math.sin(theta2 - phi) * math.sin(phi)
    dy2F = v1 * math.cos(theta1 - phi) * math.sin(phi) + v2 * math.sin(theta2 - phi) * math.cos(phi)


    print(str(dx1F) + "       dx1:")
    print(str(dy1F) + "       dy1:")
    print(str(dx2F) + "       dx2:")
    print(str(dy2F) + "       dx2:")

    balls[ball1].angle = math.degrees(math.atan2(dy1F,dx1F))
    balls[ball2].angle = math.degrees(math.atan2(dy2F,dx2F))

    balls[ball1].speed = math.sqrt(math.pow(dx1F,2) + math.pow(dy1F,2))
    balls[ball2].speed = math.sqrt(math.pow(dx2F,2) + math.pow(dy2F,2))

def CollisionDetect():
    for ball1 in balls:
        for ball2 in balls:
            if ball1 != ball2:
                if ((ball1.xpos-ball2.xpos)**2)+((ball1.ypos-ball2.ypos)**2) <= (ball1.radius+ball2.radius)**2:
                    print("")
                    print(str(balls[balls.index(ball1)].speed)+"          initial ball 1 speed")
                    print(str(balls[balls.index(ball1)].angle)+"          initial ball 1 angle")
                    print(str(balls[balls.index(ball2)].speed)+"          initial ball 2 speed")
                    print(str(balls[balls.index(ball2)].angle)+"          initial ball 2 angle")

                    BallsCollide(balls.index(ball1),balls.index(ball2))
                    print(str(balls[balls.index(ball1)].xpos) + "          ball1x: ")
                    print(str(balls[balls.index(ball1)].ypos) + "          ball1y: ")
                    print(str(balls[balls.index(ball2)].xpos) + "          ball2x: ")
                    print(str(balls[balls.index(ball2)].ypos) + "          ball2y: ")

                    print(str(balls[balls.index(ball1)].speed) + "        final ball 1 speed: ")
                    print(str(balls[balls.index(ball1)].angle) + "        final ball 1 angle: ")
                    print(str(balls[balls.index(ball2)].speed) + "        final ball 2 speed: ")
                    print(str(balls[balls.index(ball2)].angle) + "        final ball 2 angle: ")
                    return collisiondelay
    return 0

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