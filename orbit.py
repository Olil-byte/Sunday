import pygame
import environmet as env

class Orbit:
    def __init__(self, pos: pygame.math.Vector2, radius: float, color = env.default_orbital_color, width = env.default_orbital_line_width):
        self.pos = pygame.math.Vector2(pos)
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, surface.get_rect().center, self.radius, self.width)