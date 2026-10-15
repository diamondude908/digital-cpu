import pygame
import components.memory as memory

scale = 20
on_color = (230, 230, 230)
off_color = (20, 20, 20)

width = memory.display_width
height = memory.display_height

pygame.init()
screen = pygame.display.set_mode((width * scale, height * scale))
clock = pygame.time.Clock()

