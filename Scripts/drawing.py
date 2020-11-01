import sys
import pygame
import numpy
from pygame.constants import KEYDOWN
import pygame.gfxdraw
from random import choice

def main():
    pygame.init()
    pygame.display.set_caption('Drawing')

    # Setting up the display
    height = 650
    width = 650
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill((255,255,255),)

    # Assigning FPS
    FPS = 60
    FramePerSec = pygame.time.Clock()

    points = []
    colors = {'blue': (0,140,255),
              'red': (232,0,19),
              'green': (92,230,0),
              'purple': (170,0,255),
              'orange': (255,157,0),
              'black': (0,0,0),
              'white': (255,255,255),
              'grey': (217,219,222)
            }
    brush_color = colors['black']
    brush_radius = 20

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                position = event.pos
                points.append(position)
                points = points[-256:]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    screen.fill(colors['white'])
                elif event.button == 4:
                    brush_radius += 10
                    brush_radius = min(100, brush_radius)
                elif event.button == 5:
                    brush_radius -= 10
                    brush_radius = max(10, brush_radius)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    i = choice(numpy.arange(7))
                    brush_color = colors[list(colors.keys())[i]]
                    print('Brush color changed to {}'.format(list(colors.keys())[i]))
                    print
                elif event.key == pygame.K_r:
                    brush_color = colors['black']
                    print('Brush color defaulting to black')
            else:
                points = []
        
        if len(points) > 1:
            draw(screen, points, brush_color, brush_radius)

        FramePerSec.tick(FPS)

def draw(screen, points, color, width):
    """
    Rudimentary algorithm to draw a continuous line

    TODO: Fix the issue with circle radius and line width
    """
    for i in numpy.arange(len(points)):
        if i != len(points)-1:
                pygame.draw.line(screen, color, points[i], points[i+1], width*2)
        pygame.gfxdraw.filled_circle(screen, points[i][0], points[i][1], width, color)
        pygame.gfxdraw.filled_circle(screen, points[i][0], points[i][1], width, color)
    return

main()