BOUND = 10
import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros([10, 10])
        self.color = {'black': -1, 'white': 1, 'blank': 0}
        self.last_move = None
        self.blank = 0

    def set_chess(self, pos, color):
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
            self.last_move = color
            return True


default_board = Board()


