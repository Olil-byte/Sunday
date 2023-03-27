import pygame
from planet import Planet 

pygame.init()

caption = 'Sunday'
size = (640, 480)
FPS = 60

pygame.display.set_caption(caption)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

planet = Planet('sprites/sun.png', (128, 128))

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #running = False
            pygame.quit()
            exit()

def update():
    screen.fill('White')
    screen.blit(planet.image, screen.get_rect().center)
    pygame.display.update()

while running:
    handle_events()
    update()
    clock.tick(FPS)