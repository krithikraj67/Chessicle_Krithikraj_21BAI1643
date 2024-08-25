import pygame
import os
import math
from pieces import Piece
from board import Board

# Board image:
BOARD = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "board.png")), (700, 700)
)
rect = (60, 40, 687, 685)
bo = Board()


def redraw_gameWindow():
    global screen
    screen.blit(
        BOARD,
        (
            50,
            30,
        ),
    )
    bo.draw(screen)
    pygame.display.update()


def click(pos):
    """
    :return: pos (x, y) in range 0-7, 0-7
    """
    x, y = pos
    if (rect[0] < x < rect[0] + rect[2]) and (rect[1] < y < rect[1] + rect[3]):
        divX = x - rect[0]
        divY = y - rect[1]
        i = math.floor(divX / (rect[2] / 5))
        j = math.floor(divY / (rect[3] / 5))
        return "s", j, i

    elif bo.in_setup:
        if 160 <= x < 248 and 830 <= y < 880:
            return "a", "A-H1", None
        elif 258 <= x < 346 and 830 <= y < 880:
            return "a", "A-H2", None
        elif 356 <= x < 444 and 830 <= y < 880:
            return "a", "A-P1", None
        elif 454 <= x < 542 and 830 <= y < 880:
            return "a", "A-P2", None
        elif 552 <= x < 640 and 830 <= y < 880:
            return "a", "A-P3", None
        return "n", -1, -1

    else:
        if 170 <= x < 270 and 830 <= y < 880:
            return "m", 0, None
        elif 290 <= x < 390 and 830 <= y < 880:
            return "m", 1, None
        elif 410 <= x < 510 and 830 <= y < 880:
            return "m", 2, None
        elif 530 <= x < 630 and 830 <= y < 880:
            return "m", 3, None
        return "n", -1, -1


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_gameWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ch, i, j = click(pos)
                if ch == "s":
                    bo.select(i, j)
                elif ch == "m":
                    bo.move(i)
                elif ch == "a":
                    bo.add(i)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chessicle")
main()
