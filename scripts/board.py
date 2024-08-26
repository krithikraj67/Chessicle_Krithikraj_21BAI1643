from pieces import Hero1, Hero2, Pawn1, Pawn2, Pawn3
from move_panel import Panel
from move_log import MoveLog
from collections import deque


class Board:
    def __init__(self):
        self.rows = 5
        self.cols = 5

        # Gameplay
        self.active = (-1, -1)
        self.moves = []
        self.in_setup = True
        self.order_A = []
        self.order_B = []
        self.board = [[None] * self.cols for _ in range(self.rows)]
        self.logs = deque()
        self.pieces = {
            "A": 5,
            "B": 5,
        }
        self.gameOver = False
        self.winner = None

        # Networking
        self.turn = "A"

    def setup(self):
        """
        Populates the board with initial characters
        """
        for i, x in enumerate(self.order_A):
            self.board[0][i] = self.getPiece(x, 0, i)

        for i, x in enumerate(self.order_B):
            self.board[4][i] = self.getPiece(x, 4, i)

    def add(self, idx, player):
        """
        Adds a piece to the initial line up of the player board

        """
        if self.turn != player:
            return
        if player == "A":
            if idx in self.order_A:
                return
            self.order_A.append(idx)
        elif player == "B":
            if idx in self.order_B:
                return
            self.order_B.append(idx)

    def remove(self):
        """Resets initial order"""
        if self.turn == "A":
            self.order_A = []
        else:
            self.order_B = []

    def getPiece(self, key, r, c):
        """
        Returns an instance of the Piece class, under corresponding sub-class
        """
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

    def draw(self, screen, player):
        """
        Draws the board on the screen

        """

        # Playing board
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]:
                    self.board[i][j].draw(screen, self.board, player)
        if not self.in_setup:
            # Move panel
            if self.active[0] == -1 or self.active[1] == -1:
                return
            active = self.board[self.active[0]][self.active[1]]
            if not active:
                return
            panel = Panel()
            panel.draw(active, screen)

        self.draw_move_log(screen)

    def draw_move_log(self, screen):
        """
        Draws the move log
        """
        # Move Log
        move_log = MoveLog(780, 40)
        move_log.draw(screen, self.logs, self.turn)

    def select(self, r, c):
        """
        Selects the given piece
        """
        # Return if selected cell is empty or opponent's piece
        if self.board[r][c] and self.board[r][c].player != self.turn:
            return

        # Get active piece
        x, y = self.active

        # Unselect previously selected cell
        if x != -1 and y != -1 and self.board[x][y]:
            self.board[x][y].selected = False

        # Select the selected cell and get it's valid moves
        if self.board[r][c]:
            self.board[r][c].selected = True
            self.moves = self.board[r][c].valid_moves(self.board)

        # Set selected cell as active
        self.active = (r, c)

    def move(self, ind, player):
        """
        Moves selected piece to the given position
        """
        # Get active square and save it
        start = self.active
        curr = self.board[start[0]][start[1]]

        # Return if no active sqares, or starting square is empty
        if start == (-1, -1) or not curr or player != self.turn:
            return

        # Unselect starting square
        curr.selected = False

        # Get the chosen move
        delta = curr.get_moves()[ind]
        end = (start[0] + delta[0], start[1] + delta[1])

        # Return if move is not valid
        if not end in self.moves:
            return

        # Log the move in a queue. Remove least recent addition if too long
        self.logs.append(curr.get_name() + ":" + curr.get_text()[ind])
        if len(self.logs) == 15:
            self.logs.popleft()

        # Shift the piece according to chosen move (Implicitly capture enemy pieces)
        if (
            self.board[end[0]][end[1]]
            and self.board[end[0]][end[1]].player != curr.player
        ):
            self.pieces[self.board[end[0]][end[1]].player] -= 1
            if self.pieces[self.board[end[0]][end[1]].player] == 0:
                self.gameOver = True
                self.winner = curr.player
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
                if self.pieces[self.board[end[0]][end[1]].player] == 0:
                    self.gameOver = True
                    self.winner = curr.player

        # Remove piece from starting position
        self.board[start[0]][start[1]] = None

        # Change turn to the other player
        self.turn = "B" if self.turn == "A" else "A"

        # Deselect cells
        self.active = (-1, -1)
