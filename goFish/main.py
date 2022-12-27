print('loading...')
import pygame
from pygame import sprite
from time import sleep
from items import Card
from pygame.image import load

fps = 60
width, height = 700, 700
pygame.init()
print("Press the escape key to exit.")
pygame.display.set_caption("Go Fish!")

pygame.font.init() # you have to call this at the start,  if you want to use this module.
myFont = pygame.font.SysFont('Comic Sans MS', 30)

surface = pygame.display.set_mode((700, 700))
 
# Initializing RGB Color
color = (255, 255, 255)
card = pygame.sprite.Group()
screen = pygame.display.set_mode((width, height))

yOffset = 17
tmp = Card(screen, "blue", card)
tmp.rect = pygame.Rect(500, 380+yOffset, 80, 80)

# Changing surface color
surface.fill(color)
pygame.display.flip()

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                


