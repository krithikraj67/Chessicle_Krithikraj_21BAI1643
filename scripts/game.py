import pygame
import os
import math
from client import Network
from arrange_panel import ArrangePanel
from winner import Winner

# Board image:
BOARD = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "board.png")), (700, 700)
)
GAMEOVER = pygame.transform.scale(
    pygame.image.load(os.path.join("images", "gameover.png")), (700, 400)
)
rect = (60, 40, 687, 685)


def redraw_gameWindow():
    global screen, bo
    screen.blit(
        BOARD,
        (
            50,
            30,
        ),
    )
    bo.draw(screen, client.turn)
    if bo.in_setup:
        # Setup Panel
        panel = ArrangePanel()
        order = bo.order_A if client.turn == "A" else bo.order_B
        panel.draw(screen, order, client.turn)
        if len(bo.order_A) == 5:
            bo.turn = "B"
        if len(bo.order_B) == 5:
            bo.in_setup = False
            bo.setup()
            bo.turn = "A"
            bo.draw_move_log(screen)
            bo = client.send(bo)
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
        piece = None
        if 160 <= x < 248 and 790 <= y < 840:
            piece = "A-H1" if client.turn == "A" else "B-H1"
        elif 258 <= x < 346 and 790 <= y < 840:
            piece = "A-H2" if client.turn == "A" else "B-H2"
        elif 356 <= x < 444 and 790 <= y < 840:
            piece = "A-P1" if client.turn == "A" else "B-P1"
        elif 454 <= x < 542 and 790 <= y < 840:
            piece = "A-P2" if client.turn == "A" else "B-P2"
        elif 552 <= x < 640 and 790 <= y < 840:
            piece = "A-P3" if client.turn == "A" else "B-P3"
        elif 356 <= x < 451 and 875 <= y < 935:
            return "c", None, None
        return "a", piece, None

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


def connect():
    client = Network()
    client.send(client.board)
    return client.board, client


def draw_GameOver():
    global screen
    run = True
    while run:
        screen.blit(
            GAMEOVER,
            (
                180,
                130,
            ),
        )
        winner = Winner(bo.winner)
        winner.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()


def main():
    global bo
    clock = pygame.time.Clock()
    run = True
    while run:
        if bo.gameOver:
            break
        if client.turn != bo.turn:
            bo = client.send(700)
        else:
            bo = client.send(bo)
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
                    bo.move(i, client.turn)
                    bo.draw_move_log(screen)
                    if bo.gameOver:
                        bo = client.send(bo)
                elif ch == "a" and i:
                    bo.add(i, client.turn)
                elif ch == "c":
                    bo.remove()
                bo = client.send(bo)
    draw_GameOver()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chessicle")
bo, client = connect()
main()
