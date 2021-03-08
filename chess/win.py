class Win:
    def __init__(self):
        self.board = None

    def set_board(self, board):
        self.board = board

    def win_con1(self, pos):
        x, y = pos
        if self.board[x][y] != 0:
            color = self.board[x][y]
            state = 1
            for i in range(1, 5):
                y_ = y + i
                if y_ > 9 or y_ < 0:
                    break
                piece = self.board[x][y_]
                if piece == color:
                    state += 1
                else:
                    break
            for i in range(1, 5):
                y_ = y - i
                if y_ > 9 or y_ < 0:
                    break
                piece = self.board[x][y_]
                if piece == color:
                    state += 1
                else:
                    break
            if state >= 5:
                return True
        return False

    def win_con2(self, pos):
        x, y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            state = 1
            for i in range(1, 5):
                x_ = x + i
                if x_ > 9 or x_ < 0:
                    break
                piece = self.board[x_][y]
                if piece == color:
                    state += 1
                else:
                    break
            if state >= 5:
                return True
        return False

    def win_con3(self, pos):
        x, y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            state = 1
            for i in range(1, 5):
                x_, y_ = x - i, y - i
                if x_ > 9 or x_ < 0 or y_ > 9 or y_ < 0:
                    break
                piece = self.board[x_][y_]
                if piece == color:
                    state += 1
                else:
                    break
            for i in range(1, 5):
                x_, y_ = x + i, y + i
                if x_ > 9 or x_ < 0 or y_ > 9 or y_ < 0:
                    break
                piece = self.board[x_][y_]
                if piece == color:
                    state += 1
                else:
                    break
            if state >= 5:
                return True
        return False

    def win_con4(self, pos):
        x, y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            state = 1
            for i in range(1, 5):
                x_, y_ = x - i, y + i
                if x_ > 9 or x_ < 0 or y_ > 9 or y_ < 0:
                    break
                piece = self.board[x_][y_]
                if piece == color:
                    state += 1
                else:
                    break
            for i in range(1, 5):
                x_, y_ = x - i, y + i
                if x_ > 9 or x_ < 0 or y_ > 9 or y_ < 0:
                    break
                piece = self.board[x_][y_]
                if piece == color:
                    state += 1
                else:
                    break
            if state >= 5:
                return True
        return False

    def win(self, board):
        for x in range(10):
            for y in range(10):
                if board[x][y] != 0:
                    pos = [x, y]
                    color = 'black' if board[x][y] == -1 else 'white'
                    if self.win_con1(pos) or self.win_con2(pos) or self.win_con3(pos) or self.win_con4(pos):
                        return f"{color} win."
        return None
