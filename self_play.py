import numpy as np
from src.playMove import playMove, placePiece, isWin, isLoss, isDraw

def prRed(skk): return "\033[91m {}\033[00m".format(skk)
def prGreen(skk): return "\033[92m {}\033[00m".format(skk)
def prYellow(skk): return "\033[93m {}\033[00m".format(skk)
def prLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def prPurple(skk): return "\033[95m {}\033[00m".format(skk)
def prCyan(skk): return "\033[96m {}\033[00m".format(skk)
def prLightGray(skk): return "\033[97m {}\033[00m".format(skk)


boardsize = (5, 6)


<<<<<<< HEAD
icons = {1: prRed('+'), 0: prLightGray('+'), -1: prPurple('+')}
=======
icons = {1: prRed('X'), 0: prLightGray('X'), -1: prPurple('X')}
>>>>>>> 4f90ad6fab05c1f40769736dd62e53784ce54ab7


def display(board):
    print(' ' + '  '.join([str(i) for i in range(len(board[0]))]))
    print('\n'.join([' '.join([icons[item] for item in row])
                     for row in board]))


if __name__ == '__main__':
    board = np.zeros(boardsize)
    while not isWin(board) and not isLoss(board) and not isDraw(board):
        display(board)
        print('=  '*10)

        rev_board = board*-1
        comp_move = playMove(rev_board)
        rev_board = placePiece(rev_board, comp_move, player=1)
        board = rev_board*-1
        display(board)
        print('=  '*10)
        if isWin(board) or isLoss(board) or isDraw(board):
            break

        comp_move = playMove(board)
        board = placePiece(board, comp_move, player=1)
    print('FINAL')
    display(board)
