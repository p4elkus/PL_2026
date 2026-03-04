import pygame
from pygame.draw import *
import math

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 700))

bg = (255, 255, 255)  # фон
skin = (235, 190, 160)  # кожа
shirt = (255, 80, 0)  # оранжевый
hair = (200, 0, 255)  # фиолетовый
sign = (120, 255, 50)  # зеленый
eye = (80, 160, 255)  # голубой
brown = (140, 70, 20)  # коричневый
red = (255, 20, 20)  # красный
black = (0, 0, 0)

screen.fill(bg)

# руки
line(screen, skin, (150, 500), (90, 100), 20)  # Левая рука
line(screen, skin, (450, 500), (510, 100), 20)  # Правая рука

# кисти рук
circle(screen, skin, (90, 110), 25)
circle(screen, skin, (510, 110), 25)

# тело
circle(screen, shirt, (300, 650), 180)
circle(screen, black, (300, 650), 180, 1)

# левое плечо
l_sleeve = [(180, 480), (120, 510), (130, 610), (200, 630), (220, 540)]
polygon(screen, shirt, l_sleeve)
polygon(screen, black, l_sleeve, 1)

# правое плечо
r_sleeve = [(420, 480), (480, 510), (470, 610), (400, 630), (380, 540)]
polygon(screen, shirt, r_sleeve)
polygon(screen, black, r_sleeve, 1)

# волосы
num_triangles = 9
start_angle = math.pi + 0.2
end_angle = 2 * math.pi - 0.2
step = (end_angle - start_angle) / num_triangles
r_head = 150  # радиус головы
r_spike = r_head + 40  # длина волос

for i in range(num_triangles):
    a1 = start_angle + i * step
    a2 = start_angle + (i + 1) * step
    a_mid = (a1 + a2) / 2

    # координаты треугольников
    x1 = 300 + r_head * math.cos(a1)
    y1 = 380 + r_head * math.sin(a1)
    x2 = 300 + r_head * math.cos(a2)
    y2 = 380 + r_head * math.sin(a2)

    # вершина треугольников
    x3 = 300 + r_spike * math.cos(a_mid)
    y3 = 380 + r_spike * math.sin(a_mid)

    polygon(screen, hair, [(x1, y1), (x2, y2), (x3, y3)])
    polygon(screen, black, [(x1, y1), (x2, y2), (x3, y3)], 1)

# голова
circle(screen, skin, (300, 380), 150)
circle(screen, black, (300, 380), 150, 1)

# левый глаз
circle(screen, eye, (230, 340), 30)
circle(screen, black, (230, 340), 30, 1)
circle(screen, black, (230, 340), 8)  # зрачок
# правый глаз
circle(screen, eye, (370, 340), 30)
circle(screen, black, (370, 340), 30, 1)
circle(screen, black, (370, 340), 8)  # зрачок

# нос
polygon(screen, brown, [(290, 390), (310, 390), (300, 415)])
polygon(screen, black, [(290, 390), (310, 390), (300, 415)], 1)

# рот
polygon(screen, red, [(210, 440), (390, 440), (300, 510)])
polygon(screen, black, [(210, 440), (390, 440), (300, 510)], 1)

# табличка
rect(screen, sign, (20, 40, 560, 70))
rect(screen, black, (20, 40, 560, 70), 2)

font = pygame.font.SysFont('arial', 55, bold=True)
text = font.render('PYTHON is AMAZING', True, black)
screen.blit(text, (70, 45))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()