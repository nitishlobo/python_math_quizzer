import quizLib as ql

sys = ql.System()

while True:
    #Getting which operation to run
    sys.chooseOp()
    #If all q's of choosen operation have been asked then repeat question
    if (sys.opNum == -2):
        print "============================================"
        print "       PROGRAM HAS FINISHED RUNNING"
        print "============================================"
        break

    #Getting values and setting the retrived cell in the array to 0
    if (sys.opNum == 0):
        sys.add.chooseRowCol()
        n1 = sys.add.arr[0][sys.add.col]
        n2 = sys.add.arr[sys.add.row][sys.add.col]
        sys.add.arr[sys.add.row][sys.add.col] = 0
    if (sys.opNum == 1):
        sys.sub.chooseRowCol()
        n1 = sys.sub.arr[0][sys.sub.col]
        n2 = sys.sub.arr[sys.sub.row][sys.sub.col]
        sys.sub.arr[sys.sub.row][sys.sub.col] = 0
    if (sys.opNum == 2):
        sys.mul.chooseRowCol()
        n1 = sys.mul.arr[0][sys.mul.col]
        n2 = sys.mul.arr[sys.mul.row][sys.mul.col]
        sys.mul.arr[sys.mul.row][sys.mul.col] = 0
    if (sys.opNum == 3):
        sys.div.chooseRowCol()
        n1 = sys.div.arr[0][sys.div.col]
        n2 = sys.div.arr[sys.div.row][sys.div.col]
        sys.div.arr[sys.div.row][sys.div.col] = 0

    #Displaying operation question to user
    ql.displayQ(n1, n2, sys.opNum)

    #Asking user's answer. Keep asking until number is entered.
    while True:
        try:
            userAns = int(raw_input())
        except ValueError:
            print("Not a valid entry. Only numbers accepted.")
            continue
        else:
            break

    #Getting correct answer
    correctAns = ql.getResult(n1, n2, sys.opNum)

    #If user's input is correct:
    if (userAns == correctAns):
        #Score increases by 1
        sys.incPoints()

    #qRemaining decreases by 1
    sys.decQRem()

    #Display score and qRemaining
    ql.displayScore(sys.qTotalRem, sys.points)
