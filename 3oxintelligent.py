def check(board):
    resultc = 0
    resultd = 0
    for i in range(3):
        result = 0
        for j in range(3):
            result += board[3*i + j]
        if abs(result) == 6:
            return abs(result) / result

        result = 0
        for j in range(3):
            result += board[3*j + i]
        if abs(result) == 6:
            return abs(result) / result
    result = 0
    for i in range(3):
        result += board[3*i + i]
        resultd += board[3*i + (3 - i)]
        if resultc == 6 or resultd == 6:
            return 1
        if resultc == -6 or resultd == 6:
            return -1

def pinch(board):


def decrease(board):
    return []

def recur(board, my_turn, step):
