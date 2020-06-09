import sys

def switching(status):
    if status == '0':
        return '.'
    else:
        return '0'

def getAnswer(board, boardHight, boardWidth):
    shortest = -1
    answer = [x for x in range(0, 2 ** boardWidth)]
    for a in answer:
        count = 0
        
        for i in range(0, boardHight):
            for j in range(0, boardWidth):
                if i > 0 and board[i-1, j] == '0':
                    count += 1
                    board[i-1, j] = switching(board[i-1, j])
                    board[i, j] = switching(board[i, j])
                    if j > 0:
                        board[i, j-1] = switching(board[i, j-1])
                    if j < boardWidth:
                        board[i, j+1] = switching(board[i, j+1])
        

    return shortest

i = 0
boardHight = 0
boardWidth = 0
board = [[]]
for line in sys.stdin:
    if i == 0:
        boardSize = line.strip().split(' ')
        boardHight = int(boardSize[0])
        boardWidth = int(boardSize[1])
    else:
        board.append([c for c in line.strip()])

    i += 1
    if i > int(boardSize[0]):
        print(getAnswer(board, boardHight, boardWidth))
        exit()