#################################################
# writing_session5_practice_solutions.py
#################################################

import cs112_f19_week5_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def shortenLongRuns(L, k): # want to know better answer
    consecutive = 0
    newList = []
    for i in range(len(L)):
        if L[i] not in newList:
            newList.append(L[i])
            consecutive = 1
        elif L[i] == L[i-1]:
            consecutive += 1
            if consecutive >= k:
                continue
            else:
                newList.append(L[i])
        elif L[i] != L[i-1]:
            newList.append(L[i])
            consecutive = 1
    return newList
            
class SayHi():
    def __init__(self, name):
        self.name = name
        self.saidHiL = []
        self.saidHiN = []
    
    def sayHi(self, obj):
        obj.saidHiL.append(self)
        obj.saidHiN.append(self.name)
    
    def saidHiList(self):
        return self.saidHiL
        
    def saidHiNames(self):
        return self.saidHiN

def nondestructiveRemoveRowAndCol(A, row, col):
    # remember: do not copy or deepcopy A here.
    # instead, directly construct the result
    rows = len(A)
    newList = []
    for i in range(rows):
        if i == row:
            continue
        else:
            newList.append(A[i][:col] + A[i][col+1:])
    return newList

def destructiveRemoveRowAndCol(A, row, col):
    i = 0
    while i < len(A):
        if i == row:
            A.pop(i)
            row = -1 
        else:
            A[i].pop(col)
            i += 1
            
def bestQuiz(a):
    avg, summation, count = [], [0, 0, 0], [0, 0, 0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != -1:
                summation[j] += a[i][j]
                count[j] += 1
    if sum(summation) == 0:
        return None
    for k in range(len(count)):
        if count[k] != 0:
            avg.append(summation[k] / count[k])
        else:
            avg.append(0)
    return avg.index(max(avg))

def matrixAdd(L, M):
    rowL = len(L)
    colL = len(L[0])
    rowM = len(M)
    colM = len(M[0])
    newList = [[0] * colL for row in range(rowL)]
    if rowL != rowM or colL != colM:
        return None
    else:
        for i in range(rowL):
            for j in range(colL):
                newList[i][j] += (L[i][j] + M[i][j])
    return newList
            

def isMostlyMagicSquare(a):
    base = sum(a[0])
    for i in range(len(a)):
        if sum(a[i]) != base:
            return False
    for col in range(len(a[0])):
        if sum([a[j][col] for j in range(len(a))]) != base:
            return False
    sumLeft, sumRight = 0, 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j: sumLeft += a[i][j]
            if i + j == len(a) - 1:
                sumRight += a[i][j]
    if sumLeft != base or sumRight != base:
        return False
    return True

class DataTable(object):
    def __init__(self, csvString):
        # load the 2d list from the csv string
        newList = []
        for line in csvString.split("\n"):
            newList.append(line.strip().split(","))
        # and convert the strings to numbers (but skip the labels)
        newList = newList[1:-1]
        self.table = newList
        self.rows = len(newList)
        self.cols = len(newList[0])

    def getDims(self):
        return self.rows, self.cols

    def getColumn(self, columnIndex):
        return DataColumn(self.table, columnIndex)

class DataColumn(object):
    def __init__(self, dataTable, columnIndex):
        self.label = dataTable[0][columnIndex]
        if columnIndex == 0:
            self.data = [dataTable[row][columnIndex] \
                     for row in range(1,len(dataTable))]
        else:
            self.data = [int(dataTable[row][columnIndex]) \
                         for row in range(1,len(dataTable))]
    def average(self):
        return sum(self.data) / len(self.data)

#################################################
# Test Functions
#################################################

def testShortenLongRuns():
    print('Testing shortenLongRuns()...', end='')
    assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
    assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
    print("Passed!")

def testSayHiClass():
    print('Testing sayHiClass...', end='')
    harry = SayHi('A')
    ron = SayHi('B')
    hermione = SayHi('C')
    hermione.sayHi(ron)
    assert(harry.saidHiList() == [ ])
    assert(ron.saidHiList() == [ hermione ])
    assert(hermione.saidHiList() == [ ])
    hermione.sayHi(ron) # include duplicates
    harry.sayHi(ron) # and list in the order they say hi, so...
    ron.sayHi(harry)
    assert(harry.saidHiList() == [ ron ])
    assert(ron.saidHiList() == [ hermione, hermione, harry ])
    assert(hermione.saidHiList() == [ ])
    # Finally, a similar method returns the names, not the objects:
    assert(harry.saidHiNames() == [ 'B' ])
    assert(ron.saidHiNames() == [ 'C', 'C', 'A' ])
    assert(hermione.saidHiNames() == [ ])
    print('Passed!')

def testNondestructiveRemoveRowAndCol():
    print('Testing removeRowAndCol()...', end='')
    a = [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]]
    aCopy = copy.copy(a)
    assert(nondestructiveRemoveRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == aCopy)
    assert(nondestructiveRemoveRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == aCopy)
    b = [[37, 78, 29, 70, 21, 62, 13, 54, 5],
    [6,     38, 79, 30, 71, 22, 63, 14, 46],
    [47,    7,  39, 80, 31, 72, 23, 55, 15],
    [16,    48, 8,  40, 81, 32, 64, 24, 56],
    [57,    17, 49, 9,  41, 73, 33, 65, 25],
    [26,    58, 18, 50, 1,  42, 74, 34, 66], 
    [67,    27, 59, 10, 51, 2,  43, 75, 35],
    [36,    68, 19, 60, 11, 52, 3,  44, 76],
    [77,    28, 69, 20, 61, 12, 53, 4,  45]]

    c = [[37, 78, 29, 70, 21, 62,     54, 5],
    [6,     38, 79, 30, 71, 22,     14, 46],
    [47,    7,  39, 80, 31, 72,     55, 15],
    [16,    48, 8,  40, 81, 32,     24, 56],
    [57,    17, 49, 9,  41, 73,     65, 25],
    [26,    58, 18, 50, 1,  42,     34, 66], 
    [67,    27, 59, 10, 51, 2,      75, 35],
    [36,    68, 19, 60, 11, 52, 44, 76]]

    bCopy = copy.copy(b)
    assert(nondestructiveRemoveRowAndCol(b,8,6) == c)
    assert(b == bCopy)
    print('Passed!')

def testDestructiveRemoveRowAndCol():
    print("Testing destructiveRemoveRowAndCol()...", end='')
    A = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]
        ]
    B = [ [ 2, 3, 5],
          [ 0, 1, 3]
        ]
    assert(destructiveRemoveRowAndCol(A, 1, 2) == None)
    assert(A == B) # but now A is changed!
    A = [ [ 1, 2 ], [3, 4] ]
    B = [ [ 4 ] ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    A = [ [ 1, 2 ] ]
    B = [ ]
    assert(destructiveRemoveRowAndCol(A, 0, 0) == None)
    assert(A == B)
    print("Passed!")

def testBestQuiz():
    print('Testing bestQuiz()...', end='')
    a = [ [ 88,  80, 91 ],
          [ 68, 100, -1 ]]
    aCopy = copy.copy(a)
    assert(bestQuiz(a) == 2)
    assert(a == aCopy) # must be non-destructive!
    a = [ [ 88,  80, 80 ],
          [ 68, 100, 100 ]]
    assert(bestQuiz(a) == 1)
    a = [ [88, -1, -1 ],
          [68, -1, -1 ]]
    assert(bestQuiz(a) == 0)
    a = [ [-1, -1, -1 ],
          [-1, -1, -1 ]]
    assert(bestQuiz(a) == None)
    assert(bestQuiz([[]]) == None)
    print('Passed')

def testMatrixAdd():
    print('Testing matrixAdd()...', end='')
    L = [ [1,  2,  3],
          [4,  5,  6] ]
    M = [ [21, 22, 23],
          [24, 25, 26]]
    N = [ [1+21, 2+22, 3+23],
          [4+24, 5+25, 6+26]]
    lCopy = copy.copy(L)
    mCopy = copy.copy(M)
    assert(matrixAdd(L, M) == N)
    assert((L == lCopy) and (M == mCopy)) # must be non-destructive!
    assert(matrixAdd(L, [ [ 1, 2, 3] ]) == None) # dimensions mismatch
    print('Passed!')

def testIsMostlyMagicSquare():
    print("Testing isMostlyMagicSquare()...", end="")
    assert(isMostlyMagicSquare([[42]]) == True)
    assert(isMostlyMagicSquare([[2, 7, 6],
                                [9, 5, 1],
                                [4, 3, 8]]) == True)
    assert(isMostlyMagicSquare([[4-7, 9-7, 2-7],
                                [3-7, 5-7, 7-7],
                                [8-7, 1-7, 6-7]]) == True)
    a = [[7  ,12 ,1  ,14],
         [2  ,13 ,8  ,11],
         [16 ,3  ,10 ,5],
         [9  ,6  ,15 ,4]]
    assert(isMostlyMagicSquare(a))
    assert(isMostlyMagicSquare([[1, 2], [2, 1]]) == False) # bad diagonals!
    a = [[113**2, 2**2, 94**2],
         [ 82**2,74**2, 97**2],
         [ 46**2,127**2,58**2]]
    assert(isMostlyMagicSquare(a) == False) # it's close, but not quite!
    a = [[  35**2, 3495**2, 2958**2],
         [3642**2, 2125**2, 1785**2],
         [2775**2, 2058**2, 3005**2]]
    assert(isMostlyMagicSquare(a) == False) # ditto!
    print("Passed!")

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))

    column0 = dataTable.getColumn(0)
    assert(isinstance(column0, DataColumn))
    assert(column0.label == 'Name')
    assert(column0.data == ['Fred', 'Wilma'])

    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testShortenLongRuns()
    testSayHiClass()
    testNondestructiveRemoveRowAndCol()
    testDestructiveRemoveRowAndCol()
    testBestQuiz()
    testMatrixAdd()
    testIsMostlyMagicSquare()
    testDataTableAndDataColumnClasses()

def main():
    cs112_f19_week5_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
