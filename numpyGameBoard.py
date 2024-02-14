import numpy as np

class board:
    
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
    
    base = np.zeros((7,7))
    
    boardMonths = np.array([np.arange(1,7,1), np.arange(7,13,1)])
    
    boardDays = np.array([ np.arange(1,8,1) , np.arange(8,15,1) , np.arange(15,22,1) , np.arange(22,29,1) , np.arange(29,36,1) ])
    for i in range(4):
        boardDays[4][3+i] = -1
    
    
    





b = board(7, 2)
for i in range(len(b.base)):
    for j in range(len(b.base[i])):
        b.base[i][j] = 5
print(b.displayBoard())
#b.makeBoard()