import numpy as np

class board:
    base = np.zeros((7,7))
    base[0][6] = -1
    base[1][6] = -1
    base[6][3] = -1
    base[6][4] = -1
    base[6][5] = -1
    base[6][6] = -1
    boardMonths = np.array([np.arange(1,7,1), np.arange(7,13,1)])
    
    boardDays = np.array([ np.arange(1,8,1) , np.arange(8,15,1) , np.arange(15,22,1) , np.arange(22,29,1) , np.arange(29,36,1) ])
   
    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.pieces = []
        
        if self.month < 7:
            self.base[0][(self.month%6)-1] = -1
        else:
            self.base[1][(self.month%6)-1] = -1
        
        if self.day < 8:
            self.base[2][(self.day%7)-1] = -1
        elif self.day < 15:
            self.base[3][(self.day%7)-1] = -1
        elif self.day < 22:
            self.base[4][(self.day%7)-1] = -1
        elif self.day < 29:
            self.base[5][(self.day%7)-1] = -1
        else:
            self.base[6][(self.day%7)-1] = -1
    
    
    def displayBoard(self):
        display = [['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun' ], ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31]]
        for i in range(len(display)):
            row = "|"
            if i<2:
                for j in display[i]:
                 row += ' '+ str(j) + '|'
            else:
             for j in display[i]:
                  if j < 10:
                    row += " "
                  row += ' '+str(j) + " |"
            print(row)

    def getDay(self):
        return self.day
    
    def getMonth(self):
        return self.month
    

    def makeBoard(self):
        for i in range(len(self.base)):
            row = "|"
            if i<2:
                for j in self.base[i]:
                    row += ' '+ str(j) + '|'
            else:
                for j in self.base[i]:
                    if j < 10:
                        row += " "
                    row += ' '+str(j) + " |"
            print(row)
    for i in range(4):
        boardDays[4][3+i] = -1
    def createPieces(self):
        block_shape = piece(np.array([[1,1,1],[1,1,1]]))
        l_shape = piece(np.array([[1,0],[1,0],[1,0],[1,1]]))
        corner_shape = piece(np.array([[1,0,0],[1,0,0],[1,1,1]]))
        c_shape = piece(np.array([[1,1],[1,0],[1,0],[1,1]]))
        skwiggle_shape = piece(np.array([[1,0],[1,0],[1,1],[0,1]]))
        f_shape = piece(np.array([[1,0],[1,1],[1,0],[1,0]]))
        hat_shape = piece(np.array([[1,0],[1,1],[1,1]]))
        zig_shape = piece(np.array([[1,1,0],[0,1,0],[0,1,1]]))
        self.pieces = [block_shape,l_shape,corner_shape,c_shape,skwiggle_shape,f_shape,hat_shape,zig_shape]
    def placePiece(self, board, piece, x, y):
        length, width = piece.piece.shape
        ex = x+width
        ey = y + length
        if self.outbound(piece, x, y) is False:
            board[y:ey, x:ex] -= piece.piece
    def outbound(self, piece, x, y):
        if(x + piece.piece.shape[1] > 7):
            return True
        if(y + piece.piece.shape[0] > 7):
            return True
        else: return False
    def illegal(self, piece, x, y):
        boardCopy = np.copy(self.base)
        self.placePiece(boardCopy, piece, x, y)
        if -2 in boardCopy:
            return False                
        else: return True
    def solve(self, z):
        if z < 8:
            for i in range(self.base.shape[1]):
                for j in range(self.base.shape[0]):
                    if (self.outbound(self.pieces[z], i, j) is False) and (self.illegal(self.pieces[z], i, j) is True):
                        self.placePiece(self.base, self.pieces[z], i, j)
                        print(self.base)
                        self.solve(z+1)

                    



    
class piece:
    def __init__(self, piece, rot = 4):
        self.piece = piece
        self.rotations = rot
    def rotate(self):
        self.piece = np.rot90(self.piece)
    def getArray(self):
        return self.piece
    def getRot(self):
        return self.rotations
    def shape(self):
        return self.piece.shape
    





b = board(7, 2)
b.createPieces()
b.solve(0)
#print(b.outbound(b.pieces[0],2,1))

'''
print(b.displayBoard())
print(b.base)
b.createPieces()
b.placePiece(b.base, b.pieces[0], 3,6)
print(b.base)
print(b.outbound(b.pieces[0],3,4))

'''
