from pygame.image import load
import pygame
import time
from pygame import sprite
from random import choice

card = load("assets/card.png")

numToIndex = {
    'topRight':0,
    'bottomLeft':0
}
class Card(sprite.Sprite):
    def __init__(self, screen, facedown, font, group, rect):
        super().__init__()
        super().add(group)
        self.facedown = facedown
        self.font = font
        self.rect = rect
        self.owner = None
        screen = pygame.display.set_mode(self.screen_size)
