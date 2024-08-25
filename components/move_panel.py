import pygame


class Panel:
    def __init__(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), (100, 765, 600, 200))
        pygame.draw.rect(screen, (100, 200, 100), (170, 840, 100, 50))
        pygame.draw.rect(screen, (100, 200, 100), (290, 840, 100, 50))
        pygame.draw.rect(screen, (100, 200, 100), (410, 840, 100, 50))
        pygame.draw.rect(screen, (100, 200, 100), (530, 840, 100, 50))
