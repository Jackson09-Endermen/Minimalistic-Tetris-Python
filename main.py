import time
from BagRandomizer import random7bag
board = [['0' for i in range(10)] for x in range(22)]
illegalstate = False
while True:
    bag = random7bag()
    while True:
        curpiece = bag[0] # A spawning piece mechanics
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
        count = 0
        while illegalstate == False: # Gravity loop ig
            for i in curpieceonscreen:
                board[i[0] + count - 1][i[1]] = '0'
                board[i[0] + count][i[1]] = '1'
                # After this step check for illegal states
                # TODO: Put the left-right shit before getting the illegal state checks in 
                
            
            for _ in board:
                print(''.join(_))
            

            # 2 Lines at the end of every gravity loop
            count += 1
            time.sleep(1)
        #Loop back from here when the next piece spawn
