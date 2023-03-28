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

mouse_pos = (0, 0)

FPS = 60
default_time_factor = 1.0
time_factor = default_time_factor
time_factor_change_step = 0.01

default_orbital_color = pygame.Color('DarkGray')
default_orbital_line_width = 5

default_planet_sprite_size = (64, 64)

mouse_follow_mode = False
