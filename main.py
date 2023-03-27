import pygame
from planet import Planet
from orbit import Orbit

pygame.init()

caption = 'Sunday'
size = (640, 480)
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

def update():
    planets.update()

def draw():
    screen.fill('White')
    planets.draw(screen)
    pygame.display.update()

planets.add(Planet('sprites/sun.png', (64, 64), Orbit(screen.get_rect().center, 100)))

while running:
    handle_events()
    draw()
    clock.tick(FPS)
    update()
