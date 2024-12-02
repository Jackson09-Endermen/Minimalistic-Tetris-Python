#Still a hot mess of buggy code
from BagRandomizer import random7bag
board = [['0' for i in range(12)] for x in range(20)]
while True:
    bag = random7bag()
    while True:
        curpiece = bag[0]
        if curpiece == 'J':
            board[1][3] = '1'
            board[1][4] = '1'
            board[1][5] = '1'
            board[0][3] = '1'
            curpieceonscreen = [[1,3],[1,4],[1,5],[0,3]]
            pass
        elif curpiece == 'L':
            board[1][3] = '1'
            board[1][4] = '1'
            board[1][5] = '1'
            board[0][5] = '1'
            curpieceonscreen = [[1,3],[1,4],[1,5],[0,5]]
            pass
        elif curpiece == 'O':
            board[1][5] = '1'
            board[1][4] = '1'
            board[0][5] = '1'
            board[0][4] = '1'
            curpieceonscreen = [[1,5],[1,4],[0,5],[0,4]]
            pass
        elif curpiece == 'T':
            board[1][3] = '1'
            board[1][4] = '1'
            board[1][5] = '1'
            board[0][4] = '1'
            curpieceonscreen = [[1,3],[1,4],[1,5],[0,4]]
            pass
        elif curpiece == 'I':
            board[1][3] = '1'
            board[1][4] = '1'
            board[1][5] = '1'
            board[1][6] = '1'
            curpieceonscreen = [[1,3],[1,4],[1,5],[1,6]]
            pass
        elif curpiece == 'S':
            board[1][4] = '1'
            board[1][5] = '1'
            board[0][5] = '1'
            board[0][6] = '1'
            curpieceonscreen = [[1,4],[1,5],[0,5],[0,6]]
            pass
        elif curpiece == 'Z':
            board[0][4] = '1'
            board[0][5] = '1'
            board[1][5] = '1'
            board[1][6] = '1'
            curpieceonscreen = [[0,4],[0,5],[1,5],[1,6]]
            pass
        while True:
            for i in curpieceonscreen:
                board[i[0]][i[1]] = '0'
                board[i[0] + 1][i[1] + 1] = '1'
            print()  
            for _ in board:
                print(''.join(_))
