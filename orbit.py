import pygame

class Orbit:
    def __init__(self, pos: pygame.math.Vector2, radius: float):
        self.pos = pos
        self.radius = radius