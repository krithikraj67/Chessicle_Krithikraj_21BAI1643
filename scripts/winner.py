import pygame


class Winner:
    def __init__(self, winner, startX=80, startY=600) -> None:
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.winner = winner
        self.x = startX
        self.y = startY

    def draw(self, screen):
        clear_button = pygame.Rect(300, 600, 450, 160)
        pygame.draw.rect(screen, (200, 200, 200), clear_button)
        button_surface = self.font.render(
            "The winner of the game is " + self.winner, True, (0, 0, 0)
        )
        clear_rect = button_surface.get_rect(center=clear_button.center)
        screen.blit(button_surface, clear_rect)
