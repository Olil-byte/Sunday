import pygame
from planet import Planet
from orbit import Orbit

pygame.init()

caption = 'Sunday'
size = (1024, 1024)
FPS = 60

pygame.display.set_caption(caption)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

planets = pygame.sprite.Group()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #running = False
            pygame.quit()
            exit()

def draw():
    screen.fill('White')
    planets.draw(screen)
    pygame.display.update()

def update():
    clock.tick(FPS)
    planets.update()

planets.add(Planet('sprites/sun.png', (64, 64), Orbit(screen.get_rect().center, 0), 0))
planets.add(Planet('sprites/mercury.png', (64, 64), Orbit(screen.get_rect().center, 75), 4.17))
planets.add(Planet('sprites/venus.png', (64, 64), Orbit(screen.get_rect().center, 150), 1.63))
planets.add(Planet('sprites/earth.png', (64, 64), Orbit(screen.get_rect().center, 225), 1))
planets.add(Planet('sprites/mars.png', (64, 64), Orbit(screen.get_rect().center, 300), 0.53))
planets.add(Planet('sprites/jupiter.png', (64, 64), Orbit(screen.get_rect().center, 375), 0.084))
planets.add(Planet('sprites/saturn.png', (64, 64), Orbit(screen.get_rect().center, 450), 0.034))

while running:
    handle_events()
    draw()
    update()
