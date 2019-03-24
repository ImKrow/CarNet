import pygame
from src.Node import Node
from src.maptile import maptile

class Main:

    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.tile = maptile()
        self.clock = pygame.time.Clock()
        self.main_loop()
        self.map_init()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def render(self):
        self.tile.render(screen,0,0)
        self.map_init()
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            self.handle_events()
            self.render()

    def map_init(self):
        row = 12
        column = 16
        map_grid = [[0] * column for i in range (row)]
        for i in range(0,row):
            for j in range(0, column):
                map_grid[i][j] = maptile().render(screen, j*50, i*50)

    # for i in range(0, column):
    #     map_grid[i].

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    g = Main(screen)
#def render(self):




    # pygame.init()
    # x = 16
    # y = 12
    # size = [800, 600]
    # grid = [[] * y for i in range(x)]
    #
    # WHITE = (255, 255, 255)
    # BLACK = (0, 0, 0,)
    # RED = (255, 0, 0)
    #
    # screen = pygame.display.set_mode(size)
    # car = Node(3,4,5,6)
    #
    # carImg = pygame.image.load('BG_1.png')
    # clock = pygame.time.Clock()
    #
    # tile = maptile()
    #
    #
    # done = False
    #
    #
    # # for i in range(0, x):
    # #     for j in range(0, y):
    # #         grid[i].append(j)
    # #         grid[i][j] = []
    # #grid.append(tile)
    # for i in range(0,y):
    #     string = "i is equal to "
    #     string += str(i)
    #     print(string)
    #     for j in range(0,x):
    #         string2 = "j is equal to "
    #         string2 += str(j)
    #         print(string2)
    #         grid[i].insert(j,tile)
    #
    # while not done:
    #
    #     #grid[0][0].render(tile,screen,2*40, 2*40)
    #             #print(grid)
    #             #grid[0][0].render()
    #
    #
    #
    #
    #     # for i in range(0,x):
    #     #     grid[i][1].render(screen,i*40,40)
    #     clock.tick(10)
    #     screen.fill(WHITE)
    #     screen.blit(carImg, (0, 0))
    #     tile.render(screen,240,240)
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             done = True
    #
    #     pygame.display.flip()
    #
    # pygame.quit()
    # print(grid)

