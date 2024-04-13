import pygame

pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
curX = -1
curY = -1

pressed = 0
radius = 10
global i
i = 0

colorRed = (255, 0, 0)
colorBlue = (0, 0, 255)
colorGreen = (0, 255, 0)
colorBlack = (255, 255, 255)
COLOR = colorRed

print("g-green, b-blue, r-red, c-circle, t-rectangle, e-eraser")
fig = 0
FPS = 144
clock = pygame.time.Clock()
points = []

def draw(fig):
    if fig == 0:
        pygame.draw.rect(screen, COLOR, (min(prevX, curX), min(curY, prevY), abs(curX - prevX), abs(curY - prevY)), 2)
    elif fig == 1:
        xx = abs(prevX - curX)
        yy = abs(prevY - curY)
        rad = (xx * xx + yy * yy) ** 0.5
        pygame.draw.circle(screen, COLOR, (prevX, prevY), rad)

def drawLineBetween(screen, index, start, end, width):
    color = COLOR
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                COLOR = colorBlue
            if event.key == pygame.K_r:
                COLOR = colorRed
            if event.key == pygame.K_g:
                COLOR = colorGreen
            if event.key == pygame.K_t:
                fig = 0
            if event.key == pygame.K_c:
                fig = 1
            if event.key == pygame.K_e:
                fig = 2
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            prevX = event.pos[0]
            prevY = event.pos[1]
            curX = event.pos[0]
            curY = event.pos[1]
            pressed = 1

        if event.type == pygame.MOUSEMOTION:
            if pressed:
                curX = event.pos[0]
                curY = event.pos[1]
                if fig == 2:
                    COLOR = colorBlack
                    position = event.pos
                    points.append(position)
                    points = points[-len(points):]
                    while i < len(points) - 1:
                        drawLineBetween(screen, i, points[i], points[i + 1], radius)
                        i += 1
                    baseLayer.blit(screen, (0, 0))

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            i = 0
            points.clear()
            if pressed:
                curX = event.pos[0]
                curY = event.pos[1]
                pressed = 0
                baseLayer.blit(screen, (0, 0))

        if pressed:
            screen.blit(baseLayer, (0, 0))
            draw(fig)

    pygame.display.flip()
    clock.tick(FPS)