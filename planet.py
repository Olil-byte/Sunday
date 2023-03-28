import pygame
import environmet as env

from orbit import Orbit

class Planet(pygame.sprite.Sprite):
    def __init__(self, sprite_path: str, size: pygame.Rect, orbit: Orbit, speed = 1):
        pygame.sprite.Sprite.__init__(self)

        self.absolute_pos = pygame.math.Vector2()

        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.source_image = self.image
        self.rect = self.image.get_rect()

        self.orbit = orbit
        self.orbital_pos = pygame.math.Vector2(1, 0) * self.orbit.radius

        self.speed = speed

    def draw(self, surface):
        self.orbit.draw(surface)
        surface.blit(self.image, self.rect)

    def update(self):
        self.orbital_pos.rotate_ip(self.speed * env.time_factor)
        self.absolute_pos = self.orbit.pos + self.orbital_pos
        self.rect.center = self.absolute_pos

        dir_to_orbit_center = self.orbit.pos - self.absolute_pos
        angle = dir_to_orbit_center.angle_to(pygame.math.Vector2())

        correction_angle = 90

        self.image = pygame.transform.rotate(self.source_image, angle + correction_angle)
        self.rect = self.image.get_rect(center=self.absolute_pos)
