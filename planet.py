import pygame
import environmet as env

class Planet:
    def __init__(self, sprite_path: str, size = env.default_planet_sprite_size, speed = 1):
        self.pos = pygame.math.Vector2()

        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.source_image = self.image
        self.rect = self.image.get_rect()

        self.speed = speed
        self.orbital_pos = pygame.math.Vector2(1, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = self.pos
