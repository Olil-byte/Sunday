import pygame
import environmet as env

from planet import Planet
from planetary_system import PlanetarySystem

sun_system = PlanetarySystem(env.screen.get_rect().center)

sun_system.append(Planet('sprites/sun.png', speed = 0))
sun_system.append(Planet('sprites/mercury.png', speed = 4.17))
sun_system.append(Planet('sprites/venus.png', speed = 1.63))
sun_system.append(Planet('sprites/earth.png', speed = 1.0))
sun_system.append(Planet('sprites/mars.png', speed = 0.53))
sun_system.append(Planet('sprites/jupiter.png', speed = 0.084))
sun_system.append(Planet('sprites/saturn.png', speed = 0.034))
sun_system.append(Planet('sprites/uranus.png', speed = 0.012))
sun_system.append(Planet('sprites/neptune.png', speed = 0.006))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                env.mouse_follow_mode = not env.mouse_follow_mode
            if event.key == pygame.K_c:
                env.mouse_follow_mode = not env.mouse_follow_mode
                sun_system.pos = pygame.math.Vector2(env.screen.get_rect().center)
            elif event.key == pygame.K_SPACE:
                env.time_factor = env.default_time_factor

    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_PLUS]:
        env.time_factor += env.time_factor_change_step
    if keys[pygame.K_KP_MINUS]:
        env.time_factor -= env.time_factor_change_step

    move_a = 1
    if keys[pygame.K_LSHIFT]:
        move_a = 10
    if keys[pygame.K_LEFT]:
        sun_system.pos.x -= 1 * move_a
    if keys[pygame.K_RIGHT]:
        sun_system.pos.x += 1 * move_a
    if keys[pygame.K_UP]:
        sun_system.pos.y -= 1 * move_a
    if keys[pygame.K_DOWN]:
        sun_system.pos.y += 1 * move_a

    env.mouse_pos = pygame.mouse.get_pos()

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
