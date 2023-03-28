import pygame
import environmet as env

from planet import Planet
from orbit import Orbit

planets = pygame.sprite.Group()
planets.add(Planet('sprites/sun.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 0), 0))
planets.add(Planet('sprites/mercury.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 1), 4.17))
planets.add(Planet('sprites/venus.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 2), 1.63))
planets.add(Planet('sprites/earth.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 3), 1))
planets.add(Planet('sprites/mars.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 4), 0.53))
planets.add(Planet('sprites/jupiter.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 5), 0.084))
planets.add(Planet('sprites/saturn.png', (64, 64), Orbit(env.screen.get_rect().center, 64 * 6), 0.034))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_PLUS]:
        env.time_factor += env.time_factor_change_step
    if keys[pygame.K_KP_MINUS]:
        env.time_factor -= env.time_factor_change_step

def draw():
    env.screen.fill('White')
    for planet in planets:
        planet.draw(env.screen)
    pygame.display.update()

def update():
    env.clock.tick(env.FPS)
    planets.update()
    pygame.display.set_caption("{} (time factor: {})".format(env.caption, env.time_factor))

while env.running:
    handle_events()
    draw()
    update()
