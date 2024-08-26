import pygame


class Panel:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def draw(self, piece, screen):
        pygame.draw.rect(screen, (100, 100, 100), (100, 765, 600, 200))

        # Draw button
        buttons = [
            pygame.Rect(170, 840, 100, 50),
            pygame.Rect(290, 840, 100, 50),
            pygame.Rect(410, 840, 100, 50),
            pygame.Rect(530, 840, 100, 50),
        ]

        button_texts = piece.get_text()

        for idx, button in enumerate(buttons):
            pygame.draw.rect(screen, (100, 200, 100), button)

            text_surface = self.font.render(button_texts[idx], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button.center)

            screen.blit(text_surface, text_rect)
