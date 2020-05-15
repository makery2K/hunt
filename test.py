import pygame
from random import randint

pygame.init()

chicken = pygame.image.load('chicken.png')


class Chicken():
    def __init__(self):
        self.cx, self.cy = 300, 300
        self.vx, self.vy = 0, 0

    def update(self):
        if randint(1, 100) == 1:
            self.vx = randint(-10, 10)
            self.vy = randint(-10, 10)
        self.cx += self.vx
        self.cy += self.vy
        if self.cx > 800:
            self.cx = 0
        elif self.cx < 0:
            self.cx = 800
        if self.cy > 600:
            self.cy = 0
        elif self.cy < 0:
            self.cy = 600
        win.blit(chicken, (self.cx, self.cy))


win = pygame.display.set_mode((800, 600))

c1 = Chicken()
c2 = Chicken()

clock = pygame.time.Clock()
x, y = 100, 100

pygame.mouse.set_visible(False)
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event != '':
            # print(event)
            pass
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

    win.fill((100, 150, 50))
    c1.update()
    c2.update()

    pygame.draw.circle(win, (255, 255, 255), (x, y), 50, 10)
    pygame.draw.line(win, (255, 255, 255), (x, y - 80), (x, y + 80), 5)
    pygame.draw.line(win, (255, 255, 255), (x - 80, y), (x + 80, y), 5)

    pygame.display.update()

'''
    for x in range(0,800):

'''
