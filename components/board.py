import pygame
from pieces import Hero1, Hero2, Pawn1, Pawn2, Pawn3
from move_panel import Panel


class Board:
    def __init__(self):
        self.rows = 5
        self.cols = 5
        self.active = (-1, -1)
        self.moves = []

        self.board = [[None] * self.cols for _ in range(self.rows)]
        order_A = ["A-P1", "A-P2", "A-H2", "A-H1", "A-P3"]
        for i, x in enumerate(order_A):
            self.board[0][i] = self.getPiece(x, 0, i)

        order_B = ["B-P1", "B-P2", "B-H1", "B-H2", "B-P3"]
        for i, x in enumerate(order_B):
            self.board[4][i] = self.getPiece(x, 4, i)

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
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].draw(screen, self.board)
        Panel.draw(self, screen)

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
        if start == (-1, -1) or not self.board[start[0]][start[1]]:
            return
        self.board[start[0]][start[1]].selected = False
        delta = self.board[start[0]][start[1]].get_moves()[ind]
        end = (start[0] + delta[0], start[1] + delta[1])
        if not end in self.moves:
            return
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]].set_location(end)
        int_x = int((start[0] + end[0]) / 2)
        int_y = int((start[1] + end[1]) / 2)
        if start[1] != int_x or start[0] != int_y:
            if (
                self.board[int_x][int_y]
                and self.board[int_x][int_y].player
                != self.board[start[0]][start[1]].player
            ):
                self.board[int_x][int_y] = None
        self.board[start[0]][start[1]] = None
        self.active = (-1, -1)
