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
        block_shape = pieces(np.array([1,1,1],[1,1,1]))
        l_shape = pieces(np.array([1,0],[1,0],[1,0],[1,1]))
        corner_shape = pieces(np.array([1,0,0],[1,0,0],[1,1,1]))
        c_shape = pieces(np.array([1,1],[1,0],[1,0],[1,1]))
        skwiggle_shape = pieces(np.array([1,0],[1,0],[1,1],[0,1]))
        f_shape = pieces(np.array([1,0],[1,1],[1,0],[1,0]))
        hat_shape = pieces(np.array([1,0],[1,1],[1,1]))
        zig_shape = pieces(np.array([1,1,0],[0,1,0],[0,1,1]))
        self.pieces = [block_shape,l_shape,corner_shape,c_shape,skwiggle_shape,f_shape,hat_shape,zig_shape]



    
class pieces:
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

print(b.displayBoard())
print(b.base)