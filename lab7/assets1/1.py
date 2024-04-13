import pygame
import os
import datetime

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


pygame.init()

H = 917
W = 870
screen = pygame.display.set_mode((H, W))
done = False
clock = pygame.time.Clock()

c = [(H // 2) - 128 - 10, (W // 2) - 150 + 20]

ang = 0
ang2 = 0
now = datetime.datetime.now()

ang = -6 * now.second
ang2 = -6 * now.minute - 6 * (now.second / 60) 
print(now.minute, now.second)

now = datetime.datetime.now()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        ang -= 0.1
        ang2 -= 0.1 / 60

        screen.fill((0, 0, 0))
        
        screen.blit(get_image('./assets/mickeyclock.jpeg'), (0, 0))
        img = get_image('./assets/small.png')

        f = rot_center(img, ang)
        screen.blit(f, (c[0], c[1]))
        f = rot_center(img, ang2)
        screen.blit(f, (c[0], c[1]))
        
        pygame.display.flip()
        clock.tick(60)