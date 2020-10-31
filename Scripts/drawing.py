import sys
import pygame
import numpy
import pygame.gfxdraw

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
            
            else:
                points = []
        
        if len(points) > 1:
            draw(screen, points, brush_color)

        FramePerSec.tick(FPS)

def draw(screen, points, color):
    for i in numpy.arange(len(points)):
        pygame.gfxdraw.filled_circle(screen, points[i][0], points[i][1], 10, color)
        pygame.gfxdraw.filled_circle(screen, points[i][0], points[i][1], 10, color)
    
    return

main()
