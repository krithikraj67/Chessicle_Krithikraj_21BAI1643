import pygame


class MoveLog:
    def __init__(self, startX=780, startY=40):
        self.x = startX
        self.y = startY

        pygame.font.init()
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen, logs, turn):
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, 200, 750))
        for ind, log in enumerate(logs):
            move_text = self.font.render(log, True, (255, 255, 255))
            text_position = (self.x + 60, self.y + 20 + ind * 40)
            screen.blit(move_text, text_position)

        if turn == "A":
            player = "A"
            color = (200, 100, 100)
        else:
            player = "B"
            color = (100, 100, 200)

        clear_button = pygame.Rect(820, 800, 95, 60)
        pygame.draw.rect(screen, color, clear_button)
        button_surface = self.font.render(player, True, (255, 255, 255))
        clear_rect = button_surface.get_rect(center=clear_button.center)
        screen.blit(button_surface, clear_rect)
