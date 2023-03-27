import pygame
from orbit import Orbit
import math
import environmet

class Planet(pygame.sprite.Sprite):
    def __init__(self, sprite_path: str, size: pygame.Rect, orbit: Orbit, speed = 1):
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
        self.year = 0

    def update(self):
        self.angle += self.speed * environmet.speed_factor

        if self.angle >= 2 * math.pi:
            self.year += 1
            self.angle = 0
            if self.speed == 1:
                pygame.display.set_caption(environmet.caption + ': ' + str(self.year) + ' earth years')

        (x0, y0) = self.orbit.pos
        self.pos.x = x0 + math.cos(self.angle) * self.orbit.radius
        self.pos.y = y0 + math.sin(self.angle) * self.orbit.radius

        rel_x, rel_y = x0 - self.pos.x, y0 - self.pos.y
        angle1 = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        correction_angle = 90

        self.image = pygame.transform.rotate(self.source_image, angle1 + correction_angle)
        self.rect = self.image.get_rect(center=self.pos)
