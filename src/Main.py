import pygame
from src.maptile import maptile
pygame.init()

size = [800, 600]
grid = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)

screen = pygame.display.set_mode(size)
carImg = pygame.image.load('BG_1.png')
clock = pygame.time.Clock()

done = False
x = 16
y = 12
for i in range(0, x):
    grid.append([])
for i in range(0, y):
    for j in range(0, x):
        grid[i].append(j)
        grid[i][j] = 0

while not done:
    for i in range grid[0, i]:
        for j in grid[j][j]:
            tile = maptile.render(i*40, j*40)

    clock.tick(10)
    screen.fill(WHITE)
    screen.blit(carImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()

