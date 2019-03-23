import pygame

class maptile(object):

    def __init__(self):
        self.img = pygame.image.load('BG_1.png')

    def render(self, screen, x, y):
        screen.blit(self.img, (x, y))