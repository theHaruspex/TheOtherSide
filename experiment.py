from classes.user_interface import UserInterface
import pygame

pygame.init()
pygame.display.set_caption("My Game")

ui = UserInterface()

clock = pygame.time.Clock()
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the UI
    ui.update()

    # Update the display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Clean up
pygame.quit()
