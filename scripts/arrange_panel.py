import pygame


class ArrangePanel:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.button_color = {
            "A-H1": (100, 200, 100),
            "A-H2": (100, 200, 100),
            "A-P1": (100, 200, 100),
            "A-P2": (100, 200, 100),
            "A-P3": (100, 200, 100),
        }

    def draw(self, screen, order_A):
        pygame.draw.rect(screen, (100, 100, 100), (100, 765, 600, 200))

        # Draw button
        buttons = [
            pygame.Rect(160, 790, 88, 50),
            pygame.Rect(258, 790, 88, 50),
            pygame.Rect(356, 790, 88, 50),
            pygame.Rect(454, 790, 88, 50),
            pygame.Rect(552, 790, 88, 50),
        ]

        button_texts = [
            "A-H1",
            "A-H2",
            "A-P1",
            "A-P2",
            "A-P3",
        ]

        order_A = set(order_A)

        for name in button_texts:
            if name in order_A:
                self.button_color[name] = (100, 100, 200)
            else:
                self.button_color[name] = (100, 200, 100)

        for idx, button in enumerate(buttons):
            pygame.draw.rect(screen, self.button_color[button_texts[idx]], button)
            text_surface = self.font.render(button_texts[idx], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button.center)
            screen.blit(text_surface, text_rect)

        clear_button = pygame.Rect(356, 875, 95, 60)
        pygame.draw.rect(screen, (255, 100, 100), clear_button)
        button_surface = self.font.render("Clear", True, (255, 255, 255))
        clear_rect = button_surface.get_rect(center=clear_button.center)
        screen.blit(button_surface, clear_rect)
