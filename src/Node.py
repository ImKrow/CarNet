import pygame
class Node(object):

    def __init__(self):
        #self.img = pygame.image.load()
        self.x = 5
        self.y = 5
        self.speed = 30
        self.location = [self.x, self.y]

    def get_location(self):
        return [self.x,self.y]

    def get_current_speed(self):
        return self.speed

    def move(self):
        self.x = self.x+1
        self.y = self.y+1

    def render(self, screen):
        screen.blit(self.img,(self.x,self.y))
