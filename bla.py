import pygame
import sys


pygame.init()


w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Bresenham Line Drawing")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def calc(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

 
    if (x2 > x1):
        lx=1 
    else:
        lx=-1
    if (y2 > y1):
        ly=1
    else:
        ly=-1

    xk, yk = x1, y1

  
    if (dx > dy):
        pk = 2 * dy - dx
        for i in range(dx):
            screen.set_at((xk, yk), WHITE)
            xk += lx
            if pk < 0:
                pk += 2 * dy
            else:
                yk += ly
                pk += 2 * dy - 2 * dx

 
    else:
        pk = 2 * dx - dy
        for i in range(dy):
            screen.set_at((xk, yk), WHITE)
            yk += ly
            if pk < 0:
                pk += 2 * dx
            else:
                xk += lx
                pk += 2 * dx - 2 * dy



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

        
    calc(200, 100, 200, 400)
    calc(400, 100, 400, 400)
    calc(100, 200, 500, 200)
    calc(100, 300, 500, 300)

    pygame.display.flip()


