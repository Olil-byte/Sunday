import pygame

pygame.init()

running = True

icon = pygame.image.load('icon.ico')
caption = 'Sunday'
size = (1024, 1024)

pygame.display.set_icon(icon)
pygame.display.set_caption(caption)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

FPS = 60
default_time_factor = 1.0
time_factor = default_time_factor
time_factor_change_step = 0.01

default_orbital_color = pygame.Color('DarkGray')
default_orbital_line_width = 5
