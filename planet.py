import pygame
from orbit import Orbit
import math

speed_factor = 0.025

class Planet(pygame.sprite.Sprite):
    def __init__(self, sprite_path: str, size: pygame.Rect, orbit: Orbit, speed = 0.01):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.orbit = orbit
        self.rect.center = self.orbit.position
        self.speed = speed
        self.angle = 0

    def update(self):
        (x0, y0) = self.orbit.position
        self.rect.x = x0 + math.cos(self.angle) * self.orbit.radius - self.rect.width / 2
        self.rect.y = y0 + math.sin(self.angle) * self.orbit.radius - self.rect.height / 2
        self.angle += self.speed * speed_factor
