import pygame
import sys
import Colors_Dict
import random

def Square():
    pygame.init()
    window_size = (940, 880)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Move the Square')
    square_size = 50
    square_pos = [window_size[0] // 2 - square_size // 2, window_size[1] // 2 - square_size // 2]
    square_speed = 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            square_pos[0] -= square_speed
        if keys[pygame.K_RIGHT]:
            square_pos[0] += square_speed
        if keys[pygame.K_UP]:
            square_pos[1] -= square_speed
        if keys[pygame.K_DOWN]:
            square_pos[1] += square_speed

        square_pos[0] = max(0, min(square_pos[0], window_size[0] - square_size))
        square_pos[1] = max(0, min(square_pos[1], window_size[1] - square_size))
        window.fill(Colors_Dict.black)
        pygame.draw.rect(window, Colors_Dict.blue, (square_pos[0], square_pos[1], square_size, square_size))
        pygame.display.flip()
        pygame.time.Clock().tick(200)

    pygame.quit()

Square()


