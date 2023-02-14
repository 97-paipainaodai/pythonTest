theBoard = {'top-L': ' ', 'top-M':' ', 'top-R': ' ', \
    'mid-L':' ', 'mid-M':' ', 'mid-R':' ',\
    'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    newMove =input()
    if theBoard[newMove] == ' ':
        move = newMove
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print('This space is already taken, please input correct space.')

printBoard(theBoard)