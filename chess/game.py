BOUND = 10


class Board:
    def __init__(self):
        self.board = [[] * 10] * 10
        self.color = {'black': -1, 'white': 1, 'blank': 0}
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
            self.win()
            return True

    def win_con1(self, pos):
        x,y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            if y < BOUND - 5:
                state = False
                for piece in self.board[x][y+1:y+5]:
                    if piece != color:
                        return False
                return True
        return False

    def win_con2(self, pos):
        x,y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            if x < BOUND - 5:
                state = False
                for piece in self.board[x+1:x+5][y]:
                    if piece != color:
                        return False
                return True
        return False

    def win_con3(self, pos):
        x,y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            if x < BOUND - 5 and y < BOUND - 5:
                state = False
                for i in range(1,5):
                    piece = self.board[x + i][y + i]
                    if piece != color:
                        return False
                return True
        return False

    def win_con4(self, pos):
        x,y = pos
        if self.board[x][y]:
            color = self.board[x][y]
            if 3 < x and y < BOUND - 5:
                state = False
                for i in range(1,5):
                    piece = self.board[x - i][y + i]
                    if piece != color:
                        return False
                return True
        return False

    def win(self):
        for x in range(10):
            for y in range(10):
                if self.board[x][y] != 0:
                    pos = [x,y]
                    color = 'black' if self.board[x][y] ==-1 else 'white'
                    if self.win_con1([x, y]) or self.win_con2([x, y]) or self.win_con3([x, y]) or self.win_con4([x, y]):
                        return f"{color} win."
        return None


b = Board()
print(b.board)