import pygame
import environmet as env

from planet import Planet
from orbit import Orbit

class PlanetarySystem:
    def __init__(self, pos: pygame.math.Vector2):
        self.pos = pygame.math.Vector2(pos)
        self.orbits = list()
    
    def append(self, planet: Planet):
        orbit = Orbit(len(self.orbits) * planet.image.get_width(), self.pos)
        orbit.append(planet)
        self.orbits.append(orbit)

    def draw(self, surface: pygame.Surface):
        for orbit in self.orbits:
            orbit.draw(surface)

    def update(self):
        for orbit in self.orbits:
            orbit.update()

