import pygame
import random
from random import randint

pygame.init()
W = 600
H = 800



screen = pygame.display.set_mode((H, W))
done = False
image = pygame.image.load("./assets1/images.jpg")
clock = pygame.time.Clock()

songs = ["./assets1/st.mp3", "./assets1/tm.mp3", "./assets1/wk.mp3"]
cur = None
print("s-stop, n-next, p-previous, f-play")
effect = pygame.mixer.Sound(songs[0])

def inbox(x, y, sx, sy):
    if x + sx >= 0 and x + sx <= H and y + sy >= 0 and y + sy <= W:
        return 1
    return 0



def smth():
    global cur, songs, effect
    cur = randint(0, 2)
    print()
    effect = pygame.mixer.Sound(songs[cur])

def gonext():
    global songs, effect
    songs = songs[1:] + [songs[0]] # move back to the list
    effect.stop()
    effect = pygame.mixer.Sound(songs[0])
    effect.play()

def goback():
    global songs, effect
    songs = [songs[len(songs)-1]] + songs[0:len(songs)-1]
    effect.stop()
    effect = pygame.mixer.Sound(songs[0])
    effect.play()

done = False
x = 0
y = 0
play = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                effect.stop()
                play = 0
            if event.key == pygame.K_f and not play:
                effect.play()
                play = 1
            if event.key == pygame.K_n:
                gonext()
            if event.key == pygame.K_p:
                goback()
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
