BOUND = 10
import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros([10, 10])
        self.color = {'black': -1, 'white': 1, 'blank': 0}
        self.last_move = None
        self.blank = 0

    def move(self, pos, color):
        """
        :param pos:
        :param color:
        :return:
        """
        x, y = pos
        if self.board[x][y] != 0:
            return False
        else:
            self.board[x][y] = self.color[color]
            print(self.win())
            self.last_move = color
            return True

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

    def win(self):
        for x in range(10):
            for y in range(10):
                if self.board[x][y] != 0:
                    pos = [x, y]
                    color = 'black' if self.board[x][y] == -1 else 'white'
                    if self.win_con1([x, y]) or self.win_con2([x, y]) or self.win_con3([x, y]) or self.win_con4([x, y]):
                        return f"{color} win."
        return None


if __name__ == '__main__':
    b = Board()
    b.move([1, 1], 'white')
    print(b.board)
