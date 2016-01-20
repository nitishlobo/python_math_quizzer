from random import randint

class System:
    def __init__(self):
        self.points = 0
        self.qTotalRem = 576
        self.opNum = -1  #-2 = finished, -1=invalid, 0=add, 1=sub, 2=mul, 3=div

        #Keeping track of how many questions of the specific operation have been asked
        self.qOpRem = [144, 144, 144, 144]

        #Addition, subtraction, mul, div arrays
        self.add = Arrays()
        self.sub = Arrays()
        self.mul = Arrays()
        self.div = Arrays()

    def chooseOp(self):
        self.opNum = randint(0,3)
        while ((self.qOpRem[self.opNum] == 0)): #Keep repeating until you find an operation in which questions are remaining
            self.opNum = randint(0,3)
            if ((self.qOpRem[0] == 0) and (self.qOpRem[1] == 0) and (self.qOpRem[2] == 0) and (self.qOpRem[3] == 0)):
                #Program has finished running
                self.opNum = -2
                break
        return

    def decQRem(self): #Decreasing number of questions by 1 (dec. by 1 for overall and dec by 1 for specific operation)
        self.qOpRem[self.opNum] = self.qOpRem[self.opNum] - 1
        self.qTotalRem = self.qTotalRem - 1
        return

    def incPoints(self):
        self.points = self.points + 1
        return

#-----------------------------------------------------------------------------------
class Arrays:
    def __init__(self):
        #Initialising array
        self.arr = []
        for i in range (0, 13):
          self.arr.append([])
          for j in range (0, 12):
            self.arr[i].append(i)

        for j in range (0, 12):
            self.arr[0][j] = j+1

        #Initialising row and column for question
        self.row = -1 #By default it's invalid
        self.col = -1

    def chooseRowCol(self):
        while True:
            self.row = randint(1,12)
            self.col = randint(1,12)
            if (self.arr[self.row][self.col] != 0):
                break
        return

#-----------------------------------------------------------------------------------
def getResult(n1, n2, opNum):
    if (opNum == 0): #Addition
        return n1 + n2
    elif (opNum == 1): #subtraction
        return n1-n2
    elif (opNum == 2): #multiplication
        return n1 * n2
    elif (opNum == 3): #division
        return n1/n2

#-----------------------------------------------------------------------------------
def displayQ(n1, n2, opNum):
    if opNum == 0:
        opChar = "+"
    elif opNum == 1:
        opChar = "-"
    elif opNum == 2:
        opChar = "*"
    elif opNum == 3:
        opChar = "/"

    print n1, opChar, n2, "="
    return

def displayScore(qTotalRem, points):
    print "Number of questions remaining:", qTotalRem
    print "Points scored:", points
    return
