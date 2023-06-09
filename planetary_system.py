import pygame
import environmet as env

from planet import Planet

class PlanetarySystem:
    def __init__(self, pos: pygame.math.Vector2):
        self.pos = pygame.math.Vector2(pos)
        self.orbits = list()
    
    def append(self, planet: Planet):
        orbit = Orbit(self, len(self.orbits) * planet.image.get_width())
        orbit.append(planet)
        self.orbits.append(orbit)

    def draw(self, surface: pygame.Surface):
        for orbit in self.orbits:
            orbit.draw(surface)

    def update_follow_mode(self):
        if env.mouse_follow_mode:
            self.pos = pygame.math.Vector2(env.mouse_pos)

    def update(self):
        self.update_follow_mode()
        for orbit in self.orbits:
            orbit.update()

class Orbit:
    def __init__(self, system: PlanetarySystem, radius, color = env.default_orbital_color, width = env.default_orbital_line_width):
        self.system = system
        self.pos = self.system.pos
        self.radius = radius
        self.color = color
        self.width = width

    def append(self, planet: Planet):
        self.planet = planet
        self.planet.orbital_pos = pygame.math.Vector2(1, 0) * self.radius

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius, self.width)
        self.planet.draw(surface)

    def update(self):
        self.pos = self.system.pos

        self.planet.orbital_pos.rotate_ip(self.planet.speed * env.time_factor)
        self.planet.pos = self.pos + self.planet.orbital_pos

        dir_to_planet = self.pos - self.planet.pos
        angle = dir_to_planet.angle_to(pygame.math.Vector2())

        correction_angle = 90

        self.planet.update()
        self.planet.image = pygame.transform.rotate(self.planet.source_image, angle + correction_angle)
        self.planet.rect = self.planet.image.get_rect(center=self.planet.pos)