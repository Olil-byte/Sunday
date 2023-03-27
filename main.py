import pygame 

pygame.init()

caption = 'Sunday'
size = (640, 480)
FPS = 60

pygame.display.set_caption(caption)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #running = False
            pygame.quit()
            exit()

while running:
    handle_events()
    clock.tick(FPS)