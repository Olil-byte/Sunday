import pygame
from orbit import Orbit
import math
import environmet

class Planet(pygame.sprite.Sprite):
    def __init__(self, sprite_path: str, size: pygame.Rect, orbit: Orbit, speed = 0.01):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(1, 0)

        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.source_image = self.image
        self.rect = self.image.get_rect()
        self.orbit = orbit
        self.rect.center = self.orbit.pos
        self.speed = speed
        self.angle = 0

    def update(self):
        self.angle += self.speed * environmet.speed_factor

        if self.angle >= 2 * math.pi:
            self.angle = 0

        (x0, y0) = self.orbit.pos
        self.pos.x = x0 + math.cos(self.angle) * self.orbit.radius
        self.pos.y = y0 + math.sin(self.angle) * self.orbit.radius

        self.rect.center = self.pos

        #self.image = pygame.transform.rotate(self.source_image, math.degrees(self.angle))