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
            'grey': (217,219,222),
            }
    brush_color = colors['black']

    # Draw side panel
    side_panel_w = 50
    side_panel_h = height
    pygame.draw.rect(screen, colors['grey'], (0,0,side_panel_w,side_panel_h))
    #pygame.draw.rect(screen, colors['black'], (0,0,side_panel_w,side_panel_h), 2)

    # Draw bottom panel
    bottom_panel_w = width
    bottom_panel_h = 50
    pygame.draw.rect(screen, colors['grey'], 
                    (side_panel_w, height-bottom_panel_h, bottom_panel_w, bottom_panel_w))

    # Colour choises
    color_r = 15
    shift = 50
    for i in numpy.arange(5):
        pygame.gfxdraw.filled_circle(screen,
                                     int(side_panel_w/2),
                                     shift*(i+1),
                                     color_r,
                                     colors[list(colors.keys())[i]])
        pygame.gfxdraw.aacircle(screen,
                                int(side_panel_w/2),
                                shift*(i+1),
                                color_r,
                                colors['black'])

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            for i in numpy.arange(5):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                position = event.pos
                if 100<= position[0] <= 550:
                    points.append(position)
                    points = points[-256:]
            else:
                points = []
        
        if len(points) > 1:
            draw(screen, points, colors['red'])

        FramePerSec.tick(FPS)

def draw(screen, points, color):
    for i in numpy.arange(len(points)):
        pygame.draw.circle(screen, color, points[i], 20)
    
    return

main()