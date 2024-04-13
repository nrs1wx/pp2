import pygame
import random
from random import randint

pygame.init()
W = 420
H = 746

screen = pygame.display.set_mode((H, W))
done = False
clock = pygame.time.Clock()

songs = ["./assets1/st.mp3", "./assets1/tm.mp3", "./assets1/wk.mp3"]
cur = None
print("s-stop, n-next, p-previous, f-play")
effect = pygame.mixer.Sound(songs[0])

# Load an image
gif_path = "./assets1/your_gif.gif"  # Replace 'your_gif.gif' with your GIF file path
image = pygame.image.load(gif_path)

def smth():
    global cur, songs, effect
    cur = randint(0, 2)
    print()
    effect = pygame.mixer.Sound(songs[cur])

def gonext():
    global songs, effect
    songs = songs[1:] + [songs[0]]  # move back to the list
    effect.stop()
    effect = pygame.mixer.Sound(songs[0])
    effect.play()

def goback():
    global songs, effect
    songs = [songs[len(songs) - 1]] + songs[0:len(songs) - 1]
    effect.stop()
    effect = pygame.mixer.Sound(songs[0])
    effect.play()

play = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                effect.stop()
                play = False
            if event.key == pygame.K_f and not play:
                effect.play()
                play = True
            if event.key == pygame.K_n:
                gonext()
            if event.key == pygame.K_p:
                goback()

    # Draw the image on the screen
    screen.blit(image, (0, 0))  # Replace (0, 0) with the desired position to draw the image

    pygame.display.flip()
    clock.tick(60)
