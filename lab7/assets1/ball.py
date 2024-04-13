import pygame

pygame.init()
W = 600
H = 800
screen = pygame.display.set_mode((H, W))
image = pygame.image.load("./assets1/images.jpg")

screen.fill((255, 255, 255))

done = False

x = 0
y = 0

clock = pygame.time.Clock()

                    
def inbox(x, y, sx, sy):
    if x + sx >= 0 and x + sx <= H and y + sy >= 0 and y + sy <= W:
        return 1
    return 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if inbox(x + 163, y, 10, 0):
                x += 10
        if event.key == pygame.K_LEFT:
            if inbox(x, y, -10, 0):
                x -= 10
        if event.key == pygame.K_UP:
            if inbox(x, y, 0, -10):
                y -= 10
        if event.key == pygame.K_DOWN:
            if inbox(x + 163, y + 163, 0, 10):
                y += 10


    screen.fill((143, 124, 123))
    screen.blit(image, (x,y))
    
    pygame.display.flip()
    clock.tick(60)
