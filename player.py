import pygame
from settings import TILE_SIZE
from functions import scroll


class Hero:

    def __init__(self, position):
        self.x, self.y = position
        self.hero_image = pygame.image.load('data/player2.png')
        self.hero_image = pygame.transform.scale(self.hero_image, (TILE_SIZE, TILE_SIZE))
        self.hero_rect = self.hero_image.get_rect()

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        screen.blit(self.hero_image, (self.x * TILE_SIZE - scroll[0], self.y * TILE_SIZE - scroll[1]))
