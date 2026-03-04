import pygame
from pygame.draw import *
import math

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1050, 700))

# общие цвета
bg = (255, 255, 255)
skin = (235, 190, 160)
sign = (120, 255, 50)
brown = (140, 70, 20)
red = (255, 20, 20)
black = (0, 0, 0)


l_shirt = (0, 128, 0)
l_hair = (255, 255, 0)
l_eye = (190, 200, 190)


r_shirt = (255, 100, 0)
r_hair = (200, 0, 255)
r_eye = (80, 160, 255)


def draw_boy(x, shirt_color, hair_color, eye_color):
    # руки
    line(screen, skin, (x - 150, 500), (x - 210, 100), 20)  # левая рука
    line(screen, skin, (x + 150, 500), (x + 210, 100), 20)  # правая рука

    # туловище
    circle(screen, shirt_color, (x, 650), 180)
    circle(screen, black, (x, 650), 180, 1)

    # плечи
    l_sleeve = [(x - 120, 480), (x - 180, 510), (x - 170, 610), (x - 100, 630), (x - 80, 540)]
    polygon(screen, shirt_color, l_sleeve)
    polygon(screen, black, l_sleeve, 1)

    r_sleeve = [(x + 120, 480), (x + 180, 510), (x + 170, 610), (x + 100, 630), (x + 80, 540)]
    polygon(screen, shirt_color, r_sleeve)
    polygon(screen, black, r_sleeve, 1)

    # волосы
    num_triangles = 9
    start_angle = math.pi + 0.2
    end_angle = 2 * math.pi - 0.2
    step = (end_angle - start_angle) / num_triangles
    r_head = 150
    r_spike = r_head + 40

    for i in range(num_triangles):
        a1 = start_angle + i * step
        a2 = start_angle + (i + 1) * step
        a_mid = (a1 + a2) / 2

        x1 = x + r_head * math.cos(a1)
        y1 = 380 + r_head * math.sin(a1)
        x2 = x + r_head * math.cos(a2)
        y2 = 380 + r_head * math.sin(a2)
        x3 = x + r_spike * math.cos(a_mid)
        y3 = 380 + r_spike * math.sin(a_mid)

        polygon(screen, hair_color, [(x1, y1), (x2, y2), (x3, y3)])
        polygon(screen, black, [(x1, y1), (x2, y2), (x3, y3)], 1)

    # 5. Голова
    circle(screen, skin, (x, 380), 150)
    circle(screen, black, (x, 380), 150, 1)

    # 6. Глаза
    circle(screen, eye_color, (x - 70, 340), 30)
    circle(screen, black, (x - 70, 340), 30, 1)
    circle(screen, black, (x - 70, 340), 8)  # Зрачок

    circle(screen, eye_color, (x + 70, 340), 30)
    circle(screen, black, (x + 70, 340), 30, 1)
    circle(screen, black, (x + 70, 340), 8)  # Зрачок

    # 7. Нос
    polygon(screen, brown, [(x - 10, 390), (x + 10, 390), (x, 415)])
    polygon(screen, black, [(x - 10, 390), (x + 10, 390), (x, 415)], 1)

    # 8. Рот
    polygon(screen, red, [(x - 90, 440), (x + 90, 440), (x, 510)])
    polygon(screen, black, [(x - 90, 440), (x + 90, 440), (x, 510)], 1)

screen.fill(bg)


# центры
draw_boy(280, l_shirt, l_hair, l_eye)
draw_boy(770, r_shirt, r_hair, r_eye)

# кисти рук
# левые руки
circle(screen, skin, (280 - 210, 100), 25)
circle(screen, skin, (280 + 210, 100), 25)
# правые руки
circle(screen, skin, (770 - 210, 100), 25)
circle(screen, skin, (770 + 210, 100), 25)

# табличка
rect(screen, sign, (20, 20, 1010, 80))
rect(screen, black, (20, 20, 1010, 80), 2)

font = pygame.font.SysFont('arial', 80, bold=True)
text = font.render('PYTHON is REALLY AMAZING!', True, black)
screen.blit(text, (45, 15))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()