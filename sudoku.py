def printBoard(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")

def nextIndex(board, indexs):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                indexs[0] = i
                indexs[1] = j
                return True
    return False

def usedRow(board, i, j, b):
    for k in range(9):
        if(board[i][k] == b):
            return True
    return False

def usedColumn(board, i, j, b):
    for k in range(9):
        if(board[k][j] == b):
            return True
    return False

def usedSquare(board, i, j, b):
    for k in range(3):
        for p in range(3):
            if(board[k+i][p+j] == b):
                return True
    return False

def solver(board):

    indexs = [0, 0]

    if(not nextIndex(board, indexs)):
        return True

    available = guess(board, indexs[0], indexs[1])

    for b in range(1, 10):
        if(not usedRow(board, indexs[0], indexs[1], b) and not usedColumn(board, indexs[0], indexs[1], b) and not usedSquare(board, indexs[0]-indexs[0]%3, indexs[1] - indexs[1]%3, b)):
            board[indexs[0]][indexs[1]] = b

            if(solver(board)):
                return True

            board[indexs[0]][indexs[1]] = 0
    return False

def main():
    board = [[0 for i in range(9)] for j in range(9)]
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1 ,0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    solver(board)
    printBoard(board)

main()
