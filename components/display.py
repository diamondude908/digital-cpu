import pygame
import components.memory as memory

scale = 30
on_color = (230, 230, 230)
off_color = (20, 20, 20)

width = 0
height = 0
screen = None
clock = None

def init():
    global screen, clock

    width = memory.display_width
    height = memory.display_height

    pygame.init()
    screen = pygame.display.set_mode((width * scale, height * scale))
    clock = pygame.time.Clock()

def draw_pixel(x, y, on):
    if on:
        color = on_color
    else:
        color = off_color

    rect = pygame.Rect(x * scale, y * scale, scale, scale)
    pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
