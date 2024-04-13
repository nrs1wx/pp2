import pygame
import random
from random import randint
pygame.init()

score = 0
W = 720
H = 720
g = []
f = False
free = []
CELL = 60

bg=pygame.image.load('assets2/snakebg.png')
apple=pygame.image.load('assets2/apple.png')

def fill_free():
    for i in range(1, H // CELL - 1):
        for j in range(1, W // CELL - 1):
            free.append((i, j))

fill_free()

class Point:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y

    def generate():
        global free
        x = randint(0, len(free) - 1)
        for i in g:
            if free.count(i):
                free.remove(i)
        x = randint(0, len(free) - 1)

        return Point(free[x][0] * CELL, free[x][1] * CELL)

class Food:
    def __init__(self):
        self.pos = Point.generate()
    
    def draw(self):
        pygame.draw.rect(screen, colorGreen, (self.pos.X, self.pos.Y, CELL, CELL))

    def reg(self):
        self.pos = Point.generate()

class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        global g
        g = self.body
        self.dx = 0
        self.dy = 0
    
    def draw(self):
        head = self.body[0]
        for i in self.body:
            if free.count((i.X, i.Y)):
                free.remove((i.X, i.Y))
        
        pygame.draw.rect(screen, colorRed, (head.X, head.Y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorRed, (segment.X, segment.Y, CELL, CELL))

    def move(self):
        head = self.body[0]
        global g

        head.X += self.dx * CELL
        head.Y += self.dy * CELL

        if head.X == W:
            head.X = 0
        if head.X < 0:
            head.X = (W // CELL - 1) * CELL
        if head.Y == H:
            head.Y = 0
        if head.Y < 0:
            head.Y = (H // CELL - 1) * CELL

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].X = self.body[i - 1].X
            self.body[i].Y = self.body[i - 1].Y
        g = self.body
    


    def check(self, food):
        head = self.body[0]
        global g
        g = self.body


        global f
        f = True
        if head.X == food.pos.X and head.Y == food.pos.Y:
            global score
            score += 10
            f = 1
            self.body.append(Point(head.X, head.Y))
            global FPS
            FPS = 7 + (len(self.body) - 1) // 3 * 0.33
            return True

global snake
snake = Snake()

screen = pygame.display.set_mode((W, H))
FPS = 7
clock = pygame.time.Clock()


CELL = 60
colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255,255)
colorGrey = pygame.Color(128, 128, 128)
colorRed = pygame.Color(255, 0, 0)
colorGreen = pygame.Color(0, 255, 0)
colorBlue = pygame.Color(0, 0, 255)

def draw_grid():
    for i in range(0, H, CELL):
        for j in range(0, W, CELL):
            pygame.draw.rect(screen, colorGrey, (i, j, CELL, CELL), 1)

food = Food()
snake.draw()
done = False
c = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if snake.dy != 1 and event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if snake.dy != -1 and event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if snake.dx != -1 and event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if snake.dx != 1 and event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

    free.clear()
    fill_free()

    buf = Point(0, 0)
    screen.fill(colorBlack)
    if snake.check(food):
        food.reg()
        buf = snake.body[0]
    snake.move()
    if f == True and len(g) == 1:
        snake.body.append(buf)
    
    m = {}
    for i in range(0, len(g)):
        m[(g[i].X, g[i].Y)] = 0
    for i in range(0, len(g)):
        m[(g[i].X, g[i].Y)] += 1

    snake.draw()
    food.draw()
    draw_grid()

    if m[(g[0].X, g[0].Y)] > 2:
        print("SCORE:", score)
        print("LEVEL:", score // 3)
        screen.fill(colorGrey)
        pygame.display.flip()
        FPS = 0.8
        done = True
    f = False
    
    pygame.display.flip()
    clock.tick(FPS)