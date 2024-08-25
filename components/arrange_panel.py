import pygame


class ArrangePanel:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), (100, 765, 600, 200))

        # Draw button
        buttons = [
            pygame.Rect(160, 840, 88, 50),
            pygame.Rect(258, 840, 88, 50),
            pygame.Rect(356, 840, 88, 50),
            pygame.Rect(454, 840, 88, 50),
            pygame.Rect(552, 840, 88, 50),
        ]

        button_texts = [
            "A-H1",
            "A-H2",
            "A-P1",
            "A-P2",
            "A-P3",
        ]

        for idx, button in enumerate(buttons):
            pygame.draw.rect(screen, (100, 200, 100), button)
            text_surface = self.font.render(button_texts[idx], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button.center)
            screen.blit(text_surface, text_rect)
