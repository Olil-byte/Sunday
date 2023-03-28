import pygame
import environmet as env

from planet import Planet
from orbit import Orbit
from planetary_system import PlanetarySystem

sun_system = PlanetarySystem(env.screen.get_rect().center)

sun_system.append(Planet('sprites/sun.png', (64, 64), 0))
sun_system.append(Planet('sprites/mercury.png', (64, 64), 4.17))
sun_system.append(Planet('sprites/venus.png', (64, 64), 1.63))
sun_system.append(Planet('sprites/earth.png', (64, 64), 1.0))
sun_system.append(Planet('sprites/mars.png', (64, 64), 0.53))
sun_system.append(Planet('sprites/jupiter.png', (64, 64), 0.084))
sun_system.append(Planet('sprites/saturn.png', (64, 64), 0.034))

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
    if keys[pygame.K_SPACE]:
        env.time_factor = env.default_time_factor

def draw():
    env.screen.fill('White')
    sun_system.draw(env.screen)
    pygame.display.update()

def update():
    env.clock.tick(env.FPS)
    sun_system.update()
    pygame.display.set_caption("{} (time factor: {})".format(env.caption, env.time_factor))

while env.running:
    handle_events()
    draw()
    update()
