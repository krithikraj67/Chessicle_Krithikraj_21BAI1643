import pygame
from pieces import Hero1, Hero2, Pawn1, Pawn2, Pawn3
from move_panel import Panel
from arrange_panel import ArrangePanel
from collections import deque


class Board:
    def __init__(self):
        self.rows = 5
        self.cols = 5
        self.active = (-1, -1)
        self.moves = []
        self.in_setup = True
        self.order_A = []
        self.order_B = ["B-P1", "B-P2", "B-H1", "B-H2", "B-P3"]
        self.board = [[None] * self.cols for _ in range(self.rows)]
        self.logs = deque()

        pygame.font.init()
        self.font = pygame.font.Font(None, 32)

    def setup(self):
        for i, x in enumerate(self.order_A):
            self.board[0][i] = self.getPiece(x, 0, i)

        for i, x in enumerate(self.order_B):
            self.board[4][i] = self.getPiece(x, 4, i)

    def add(self, idx):
        if idx in self.order_A:
            return
        self.order_A.append(idx)
        if len(self.order_A) == 5:
            self.in_setup = False
            self.setup()

    def getPiece(self, key, r, c):
        if key[2:] == "H1":
            return Hero1(r, c, key[0])
        elif key[2:] == "H2":
            return Hero2(r, c, key[0])
        elif key[2:] == "P1":
            return Pawn1(r, c, key[0])
        elif key[2:] == "P2":
            return Pawn2(r, c, key[0])
        elif key[2:] == "P3":
            return Pawn3(r, c, key[0])

    def draw(self, screen):
        # Playing board
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].draw(screen, self.board)
        if not self.in_setup:
            # Move panel
            if self.active[0] == -1 or self.active[1] == -1:
                return
            active = self.board[self.active[0]][self.active[1]]
            if not active:
                return
            panel = Panel()
            panel.draw(active, screen)
        else:
            # Setup Panel
            panel = ArrangePanel()
            panel.draw(screen)

        # Move Log
        logStartX, logStartY = 780, 40
        pygame.draw.rect(screen, (100, 100, 100), (logStartX, logStartY, 200, 940))
        for ind, log in enumerate(self.logs):
            move_text = self.font.render(log, True, (255, 255, 255))
            text_position = (logStartX + 60, logStartY + 20 + ind * 40)
            screen.blit(move_text, text_position)

    def select(self, r, c):
        x, y = self.active
        if x != -1 and y != -1 and self.board[x][y]:
            self.board[x][y].selected = False
        if self.board[r][c]:
            self.board[r][c].selected = True
            self.moves = self.board[r][c].valid_moves(self.board)
        self.active = (r, c)

    def move(self, ind):
        start = self.active
        curr = self.board[start[0]][start[1]]
        if start == (-1, -1) or not curr:
            return
        curr.selected = False
        delta = curr.get_moves()[ind]
        end = (start[0] + delta[0], start[1] + delta[1])
        if not end in self.moves:
            return

        self.logs.append(curr.get_name() + ":" + curr.get_text()[ind])
        if len(self.logs) == 15:
            self.logs.popleft()

        self.board[end[0]][end[1]] = curr
        self.board[end[0]][end[1]].set_location(end)
        int_x = int((start[0] + end[0]) / 2)
        int_y = int((start[1] + end[1]) / 2)
        if start[1] != int_x or start[0] != int_y:
            if (
                self.board[int_x][int_y]
                and self.board[int_x][int_y].player != curr.player
            ):
                self.board[int_x][int_y] = None
        curr = None
        self.active = (-1, -1)
