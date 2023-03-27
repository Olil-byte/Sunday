import pygame

class Planet(pygame.sprite.Sprite):
    def __init__(self, sprite_path: str, size: pygame.Rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()