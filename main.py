import os
import pygame

from classes.game import Game
from classes.dialog.scene import Scene

MONITOR_WIDTH = 1024
MONITOR_HEIGHT = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-MONITOR_WIDTH},{0}"
dimensions = MONITOR_WIDTH, MONITOR_HEIGHT

# if __name__ == '__main__':
#     game = Game(dimensions)
#     game.run()

pygame.init()
screen = pygame.display.set_mode(dimensions, pygame.FULLSCREEN)

scene = Scene()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    scene.render(screen)

