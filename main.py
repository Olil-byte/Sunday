import pygame
from planet import Planet
from orbit import Orbit
import environmet
import math

pygame.init()

pygame.display.set_caption(environmet.caption)
screen = pygame.display.set_mode(environmet.size)
clock = pygame.time.Clock()

running = True

planets = pygame.sprite.Group()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_PLUS]:
            environmet.time_factor += environmet.time_factor_change_step
        if keys[pygame.K_KP_MINUS]:
            environmet.time_factor -= environmet.time_factor_change_step

def draw():
    screen.fill('White')
    for planet in planets:
        pygame.draw.circle(screen, 'Gray', screen.get_rect().center, planet.orbit.radius, environmet.orbit_line_width)
    planets.draw(screen)
    pygame.display.update()

def update():
    clock.tick(environmet.FPS)
    planets.update()
    pygame.display.set_caption(environmet.caption + ', time factor is ' + str(environmet.time_factor))

planets.add(Planet('sprites/sun.png', (64, 64), Orbit(screen.get_rect().center, 64 * 0), 0))
planets.add(Planet('sprites/mercury.png', (64, 64), Orbit(screen.get_rect().center, 64 * 1), 4.17))
planets.add(Planet('sprites/venus.png', (64, 64), Orbit(screen.get_rect().center, 64 * 2), 1.63))
planets.add(Planet('sprites/earth.png', (64, 64), Orbit(screen.get_rect().center, 64 * 3), 1))
planets.add(Planet('sprites/mars.png', (64, 64), Orbit(screen.get_rect().center, 64 * 4), 0.53))
planets.add(Planet('sprites/jupiter.png', (64, 64), Orbit(screen.get_rect().center, 64 * 5), 0.084))
planets.add(Planet('sprites/saturn.png', (64, 64), Orbit(screen.get_rect().center, 64 * 6), 0.034))

while running:
    handle_events()
    draw()
    update()
