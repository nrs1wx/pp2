import pygame
import os
import random, time
import sys
pygame.init()

colorBlack = pygame.Color(0,0,0)
colorWhite = pygame.Color(255, 255,255)
colorGrey = pygame.Color(128, 128, 128)
colorBlue = pygame.Color(0,0,255)
colorRed = pygame.Color(255,0,0)
colorGreen = pygame.Color(0,255,0)
fps = pygame.time.Clock()
fps.tick(60)
SCORE = 0
COINS = 0

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(colorWhite)
pygame.display.set_caption("RAcEr")
SPEED = 5
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./assets3/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 1
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        self.cost = random.randint(1, 3)
        super().__init__()
        self.image = pygame.image.load("./assets3/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(9, SCREEN_WIDTH-9), 560 - 13)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def reg(self):
        self.rect.center = (random.randint(9, SCREEN_WIDTH-9), 560 - 13)
        self.cost = random.randint(1, 3)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./assets3/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 540)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
C = Coin()
clock = pygame.time.Clock()
FPS = 30

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
CC = pygame.sprite.Group()
CC.add(C) #sprite group for coins

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBlack)

done = False
background = pygame.image.load("./assets3/AnimatedStreet.png")

print(type(Player))
while not done:
    N = random.randint(5, 10)
    SPEED = 5 + COINS // N #recalculate speed using the number of coins
    scores = font_small.render(str(SCORE), True, colorBlack)
    n_c = font_small.render(str(COINS), True, colorBlack)
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(n_c, (370, 10)) #display the number of coins

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    P1.update()
    E1.move()

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if type(entity) == Enemy:
            entity.move()
    
    if pygame.sprite.spritecollideany(P1, CC):
        for entity in CC: #add 1 to counter after collision + regenerate coin
            COINS += entity.cost
            entity.reg()
    
    pygame.display.update()
    clock.tick(FPS)