from src.Node import Node
import pygame


class Main():
    RED = (100,0,150)
    GREEN = (0, 175, 0)
    BLUE = (0, 0 , 255)
    game = pygame
    game.init()
    display_width = 800
    display_height = 600
    window = game.display.set_mode((display_width,display_height))
    car = Node(1, 2, 3)


    print(car.get_current_speed())
    print(car.get_location())

    
    clock = game.time.Clock()
    playing = True

    while playing:
        clock.tick(60)
        for event in game.event.get():
            if event.type == game.QUIT:
                playing = False

        car.render(window)
        window.fill(GREEN)
        game.display.update()


    game.quit()