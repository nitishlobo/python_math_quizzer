class ArrayTesting:
    def __init__(self):
        self.a = []
        for i in range (0, 13):
          self.a.append([])
          for j in range (0, 12):
            self.a[i].append(i)

        for j in range (0, 12):
            self.a[0][j] = j+1

    def print2DArray(self):
        for value in self.a:
            # Print each row's length and its elements.
            print(len(value), value)
        return


print "Addition array testing"
addArray = ArrayTesting()

print "PRINTING NEW ARRAY:"
addArray.print2DArray()

print "CHANGED ROW 12 AND COLUMN 0 TO 59999:"
addArray.a[12][0] = 59999
addArray.print2DArray()
