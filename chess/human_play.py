from board import Board, default_board


class Player:
    def __init__(self, board: Board = default_board, color='white'):
        self.color = color
        self.board = board

    def get_cur_board(self):
        return self.board.board

    def move(self, pos):
        """
        :param pos:
        :param color:
        :return:
        """
        self.board.set_chess(pos, self.color)

    def think(self):
        """
        根据棋盘判断应该往哪里下
        :return:
        """
        board = self.get_cur_board()
        pos = [0, 0]
        return pos

    def bot_move(self):
        pos = self.think()
        self.move(pos)


class BOT(object):
    def __init__(self):
        pass
    def cut_off(self):
        pass





