

board = [['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun' ], ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31]]
piece1 = [["■"],["■"],["■"],["■","■"]]
piece2 = [["■"," ","■"], ["■","■","■"]]
piece3 = [["■"],["■"],["■","■"],[" ","■"]]
piece4 = [[" ", " ", "■"],["■","■","■"], ["■"]]
piece5 = [["■","■","■"], ["■"], ["■"]]
piece6 = [["■"], ["■","■"], ["■"], ["■"]]
piece7 = [["■","■","■"],["■","■","■"]]
piece8 = [["■","■"],["■","■"],["■"]]
pieces = [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8]

def printPiece(array):
    for i in range(len(array)):
        row = ""
        for i in array[i]:
            row += i
        print(row)
def makeBoard():
    for i in range(len(board)):
        row = "|"
        if i<2:
            for j in board[i]:
                row += ' '+j + '|'
        else:
            for j in board[i]:
                if j < 10:
                    row += " "
                row += ' '+str(j) + " |"
        print(row)
def printPieces():
    for i in range(len(pieces)):
        printPiece(pieces[i])
        print("")
printPieces()
makeBoard()

