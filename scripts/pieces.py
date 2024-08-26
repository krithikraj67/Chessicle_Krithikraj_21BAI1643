import pygame
import os

# A pieces:
A_H1 = pygame.image.load(os.path.join("images", "A-H1.png"))
A_H2 = pygame.image.load(os.path.join("images", "A-H2.png"))
A_P1 = pygame.image.load(os.path.join("images", "A-P1.png"))
A_P2 = pygame.image.load(os.path.join("images", "A-P2.png"))
A_P3 = pygame.image.load(os.path.join("images", "A-P3.png"))

# B pieces:
B_H1 = pygame.image.load(os.path.join("images", "B-H1.png"))
B_H2 = pygame.image.load(os.path.join("images", "B-H2.png"))
B_P1 = pygame.image.load(os.path.join("images", "B-P1.png"))
B_P2 = pygame.image.load(os.path.join("images", "B-P2.png"))
B_P3 = pygame.image.load(os.path.join("images", "B-P3.png"))

# Array formats:
A = [A_H1, A_H2, A_P1, A_P2, A_P3]
B = [B_H1, B_H2, B_P1, B_P2, B_P3]

# Names
A_names = ["A_H1", "A_H2", "A_P1", "A_P2", "A_P3"]
B_names = ["B_H1", "B_H2", "B_P1", "B_P2", "B_P3"]


# Resize images:
def resize(img):
    return pygame.transform.scale(img, (120, 120))


A = list(map(resize, A))
B = list(map(resize, B))


class Piece:
    img = -1
    rect = (57, 37, 687, 685)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
        self.selected = False

    def set_location(self, loc):
        x, y = loc
        self.row = x
        self.col = y

    def valid_moves(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, screen, board, player):
        if self.player == "A":
            drawThis = A[self.img]
        else:
            drawThis = B[self.img]

        if self.selected and player == self.player:
            moves = self.valid_moves(board)

            for r, c in moves:
                x = round(self.startX + (c * self.rect[2] / 5))
                y = round(self.startY + (r * self.rect[3] / 5))
                pygame.draw.rect(
                    screen,
                    (
                        0,
                        255,
                        0,
                    ),
                    (x + 5, y + 5, 130, 130),
                )

        x = round(self.startX + (self.col * self.rect[2] / 5))
        y = round(self.startY + (self.row * self.rect[3] / 5))

        if self.selected:
            pygame.draw.rect(
                screen,
                (
                    0,
                    0,
                    255,
                ),
                (x + 5, y + 5, 130, 130),
            )
        screen.blit(drawThis, (x + 10, y + 10))


class Hero1(Piece):
    img = 0

    def __init__(self, row, col, player):
        super().__init__(row, col, player)

    def get_name(self):
        if self.player == "A":
            arr = A_names
        else:
            arr = B_names
        return arr[self.img]

    def get_moves(self):
        if self.player == "B":
            return [[0, -2], [0, 2], [-2, 0], [2, 0]]
        return [[0, -2], [0, 2], [2, 0], [-2, 0]]

    def get_text(self):
        return ["L", "R", "F", "B"]

    def valid_moves(self, board):
        i, j = self.row, self.col
        moves = []

        for dr, dc in self.get_moves():
            r, c = i + dr, j + dc
            if (
                0 <= r < 5
                and 0 <= c < 5
                and ((not board[r][c]) or board[r][c].player != self.player)
            ):
                moves.append((r, c))
        return moves


class Hero2(Piece):
    img = 1

    def __init__(self, row, col, player):
        super().__init__(row, col, player)

    def get_name(self):
        if self.player == "A":
            arr = A_names
        else:
            arr = B_names
        return arr[self.img]

    def get_moves(self):
        if self.player == "B":
            return [
                [-2, -2],
                [-2, 2],
                [2, -2],
                [2, 2],
            ]
        return [[2, -2], [2, 2], [-2, -2], [-2, 2]]

    def get_text(self):
        return ["FL", "FR", "BL", "BR"]

    def valid_moves(self, board):
        i, j = self.row, self.col
        moves = []
        dirs = [[2, 2], [2, -2], [-2, 2], [-2, -2]]
        for dr, dc in dirs:
            r, c = i + dr, j + dc
            if (
                0 <= r < 5
                and 0 <= c < 5
                and ((not board[r][c]) or board[r][c].player != self.player)
            ):
                moves.append((r, c))
        return moves


class Pawn(Piece):
    def __init__(self, row, col, player):
        super().__init__(row, col, player)

    def get_moves(self):
        if self.player == "B":
            return [[0, -1], [0, 1], [-1, 0], [1, 0]]
        return [[0, -1], [0, 1], [1, 0], [-1, 0]]

    def get_text(self):
        return ["L", "R", "F", "B"]

    def valid_moves(self, board):
        i, j = self.row, self.col
        moves = []

        for dr, dc in self.get_moves():
            r, c = i + dr, j + dc
            if (
                0 <= r < 5
                and 0 <= c < 5
                and ((not board[r][c]) or board[r][c].player != self.player)
            ):
                moves.append((r, c))
        return moves


class Pawn1(Pawn):
    img = 2

    def get_name(self):
        if self.player == "A":
            arr = A_names
        else:
            arr = B_names
        return arr[self.img]


class Pawn2(Pawn):
    img = 3

    def get_name(self):
        if self.player == "A":
            arr = A_names
        else:
            arr = B_names
        return arr[self.img]


class Pawn3(Pawn):
    img = 4

    def get_name(self):
        if self.player == "A":
            arr = A_names
        else:
            arr = B_names
        return arr[self.img]
