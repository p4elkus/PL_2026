import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

# фон
screen.fill((210, 210, 210))

# лицо
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1) # контур

# глаза
circle(screen, (255, 0, 0), (160, 170), 22)
circle(screen, (0, 0, 0), (160, 170), 22, 1) # контур
circle(screen, (255, 0, 0), (240, 170), 22)
circle(screen, (0, 0, 0), (240, 170), 22, 1) # контур

# зрачки
circle(screen, (0, 0, 0), (160, 170), 8)
circle(screen, (0, 0, 0), (240, 170), 8)

# левая бровь
polygon(screen, (0, 0, 0), [
    (100, 100),  # верхний левый угол
    (182, 145),  # верхний правый угол
    (182, 160),  # нижний правый угол
    (100, 115)   # нижний левый угол
])

# правая бровь
polygon(screen, (0, 0, 0), [
    (218, 140),  # верхний левый угол
    (285, 120),  # верхний правый угол
    (285, 135),  # нижний правый угол
    (218, 155)   # нижний левый угол
])

# рот
rect(screen, (0, 0, 0), (150, 240, 110, 15))

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()