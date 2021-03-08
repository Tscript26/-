from game import Board
from human_play import Player


def play():
    board = Board()
    A, B = Player(board, 'white'), Player(board, 'black')


if __name__ == '__main__':
    play()
