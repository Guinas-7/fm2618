import pygame, sys
from time import sleep
from pygame.locals import *
import random,math
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Billiards")

timer=0
collisiondelay = 500

FPS = 120
screenx = 1000
screeny = 800
screen = pygame.display.set_mode((screenx, screeny))

tabledimentions = (50,150,950,650)
wallwith = 25


ballradius = 18
balldrag = 0.01

holeradius = 2*ballradius


tablecenterx = (tabledimentions[2]-tabledimentions[0])/2 + tabledimentions[0]
tablecentery = (tabledimentions[3]-tabledimentions[1])/2 + tabledimentions[1]
triagleoriginx = tablecenterx+(tabledimentions[2]-tablecenterx)/2


class ball:

    def __init__(self, color, type, angle, speed,x,y):
        self.type = type
        self.color = color
        self.xpos = x
        self.ypos = y
        self.angle = angle
        self.speed = speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.xpos), int(self.ypos)), ballradius + 1,0)

    def move(self):
        self.xpos += self.speed*math.cos(math.radians(self.angle))
        self.ypos += self.speed*math.sin(math.radians(self.angle))

    def slowdown(self):
        if self.speed > 0:
            self.speed -= balldrag
        if self.speed < 0:
            self.speed = 0

    def ballcolision(self,ball2):
        print("colision")
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


class line:
    def __init__(self, ix, iy, fx, fy):
        self.initialx = ix
        self.initialy = iy
        self.finalx = fx
        self.finaly = fy
        self.color = (255,255,255)

    def draw(self):
        pygame.draw.line(screen, self.color, [self.initialx, self.initialy], [self.finalx, self.finaly], 1)




class hole:
    def __init__(self,x,y,radius):
        self.xpos = x
        self.ypos = y
        self.radius = holeradius + radius

    def draw(self):
        pygame.draw.circle(screen, (0, 50, 0), (int(self.xpos), int(self.ypos)), self.radius, 0)


balls = [ball((255, 255, 255), "white", 0, 0, 400, tablecentery),
         ball((  0, 200, 200), "other", 0, 0, triagleoriginx + 1 * ballradius - 1, tablecentery),
         ball((  0,   0, 200), "other", 0, 0, triagleoriginx + 3 * ballradius - 2, tablecentery + ballradius + 2),
         ball((150,   0,   0), "other", 0, 0, triagleoriginx + 3 * ballradius - 2, tablecentery - ballradius - 2),
         ball((200,   0, 200), "other", 0, 0, triagleoriginx + 5 * ballradius - 3, tablecentery),
         ball((200,   0,   0), "other", 0, 0, triagleoriginx + 5 * ballradius - 3, tablecentery + 2 * ballradius + 3),
         ball(( 50,   0,   0), "other", 0, 0, triagleoriginx + 5 * ballradius - 3, tablecentery - 2 * ballradius - 3),
         ball((100,   0,   0), "other", 0, 0, triagleoriginx + 7 * ballradius - 4, tablecentery + 3 * ballradius + 4),
         ball((  0,   0,   0), "other", 0, 0, triagleoriginx + 7 * ballradius - 4, tablecentery + ballradius + 2),
         ball((  0, 200, 200), "other", 0, 0, triagleoriginx + 7 * ballradius - 4, tablecentery - ballradius - 2),
         ball((  0,   0, 200), "other", 0, 0, triagleoriginx + 7 * ballradius - 4, tablecentery - 3 * ballradius - 4),
         ball((150,   0,   0), "other", 0, 0, triagleoriginx + 9 * ballradius - 5, tablecentery),
         ball((200,   0, 200), "other", 0, 0, triagleoriginx + 9 * ballradius - 5, tablecentery + 2 * ballradius + 3),
         ball((200,   0,   0), "other", 0, 0, triagleoriginx + 9 * ballradius - 5, tablecentery + 4 * ballradius + 5),
         ball(( 50,   0,   0), "other", 0, 0, triagleoriginx + 9 * ballradius - 5, tablecentery - 4 * ballradius - 5),
         ball((100,   0,   0), "other", 0, 0, triagleoriginx + 9 * ballradius - 5, tablecentery - 2 * ballradius - 3)
         ]


walls = [wall(tabledimentions[0],tabledimentions[1],tabledimentions[2],wallwith,"horizontal"),
         wall(tabledimentions[0],tabledimentions[3]- wallwith,tabledimentions[2],wallwith,"horizontal"),
         wall(tabledimentions[0],tabledimentions[1],wallwith,tabledimentions[3]-tabledimentions[1],"vertical"),
         wall(tabledimentions[2]-wallwith,tabledimentions[1],wallwith,tabledimentions[3]-tabledimentions[1],"vertical")]

holes = [hole(tabledimentions[0] - 7, tabledimentions[1] - 7, 4),
         hole(tabledimentions[0] - 7, tabledimentions[3] + 7, 4),
         hole(tabledimentions[2] + 7, tabledimentions[1] - 7, 4),
         hole(tabledimentions[2] + 7, tabledimentions[3] + 7, 4),
         hole(tablecenterx, tabledimentions[1] - 10, -7),
         hole(tablecenterx, tabledimentions[3] + 10, -7)
         ]

lines = [#LU
    line(tabledimentions[0], tabledimentions[1] - holeradius, tabledimentions[0] + holeradius + wallwith, tabledimentions[1] + wallwith),
    line(tabledimentions[0] - holeradius, tabledimentions[1], tabledimentions[0] + wallwith, tabledimentions[1] + holeradius + wallwith),
         #LD
    line(tabledimentions[0], tabledimentions[3] + holeradius, tabledimentions[0] + holeradius + wallwith, tabledimentions[3] - wallwith),
    line(tabledimentions[0] - holeradius, tabledimentions[3], tabledimentions[0] + wallwith, tabledimentions[3] - holeradius - wallwith),
         #RU
    line(tabledimentions[2], tabledimentions[1] - holeradius, tabledimentions[2] - holeradius - wallwith, tabledimentions[1] + wallwith),
    line(tabledimentions[2] + holeradius, tabledimentions[1], tabledimentions[2] - wallwith, tabledimentions[1] + holeradius + wallwith),
         #RD
    line(tabledimentions[2], tabledimentions[3] + holeradius, tabledimentions[2] - holeradius - wallwith, tabledimentions[3] - wallwith),
    line(tabledimentions[2] + holeradius, tabledimentions[3], tabledimentions[2] - wallwith, tabledimentions[3] - holeradius - wallwith),


         ]


def collisiondetect():
    for i in range(len(balls)):
            for j in range(i+1, len(balls)):
                    if ((balls[i].xpos-balls[j].xpos)**2)+((balls[i].ypos-balls[j].ypos)**2) <= (ballradius+ballradius)**2:
                        balls[i].ballcolision(j)
    return


def isballmoving():
    i = 0
    while i < len(balls):
        if balls[i].speed > 0:
            return True
        i += 1
    return False


def movewhiteball():
    xmouse = pygame.mouse.get_pos()[0]
    ymouse = pygame.mouse.get_pos()[1]
    distance = math.sqrt(((balls[0].xpos - xmouse) ** 2) + ((balls[0].ypos - ymouse) ** 2))
    if pygame.mouse.get_pressed()[0]:
        balls[0].angle = math.degrees(math.atan2(balls[0].ypos - ymouse,balls[0].xpos - xmouse))
        distance = math.sqrt(((balls[0].xpos - xmouse) ** 2) + ((balls[0].ypos - ymouse) ** 2))
        if distance > 150:
            distance = 150
        balls[0].speed = distance/30
    print(distance)


while True:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    # drawtable
    pygame.draw.rect(screen, (51,102,0), pygame.Rect(tabledimentions[0], tabledimentions[1], tabledimentions[2]-tabledimentions[0], tabledimentions[3]-tabledimentions[1]))


    i = 0
    while i < len(balls):
        if balls[i].xpos-ballradius <= tabledimentions[0] or balls[i].xpos+ballradius >= tabledimentions[2]:
            balls[i].angle = math.degrees(math.pi - math.radians(balls[i].angle))
        if balls[i].ypos-ballradius <= tabledimentions[1] or balls[i].ypos+ballradius >= tabledimentions[3]:
            balls[i].angle = math.degrees(-math.radians(balls[i].angle))
        balls[i].draw()
        balls[i].move()
        balls[i].slowdown()
        i += 1

    i = 0
    while i < len(walls):
        #walls[i].draw()
        i += 1

    i = 0
    while i < len(holes):
        holes[i].draw()
        i += 1

    i = 0
    while i < len(lines):
        lines[i].draw()
        i += 1


    if isballmoving():
        collisiondetect()
    else:
        movewhiteball()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
