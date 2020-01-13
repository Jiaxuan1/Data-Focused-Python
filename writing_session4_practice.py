#################################################
# writing_session4_practice_solutions.py
#################################################

import cs112_f19_week4_linter
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

# From Quiz 3
def getAverage(s):
    s = s.split(",")
    count = 0
    sum = 0
    for i in s:
        if i.isdigit() and int(i) >= 0:
            count += 1
            sum += int(i)
    if count == 0:
        return None
    else:
        return sum / count

import string
def encode(s):
    source = "ABCD"
    reference = 0
    newstring = ""
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            newstring += source[reference] + s[i]
            if reference == 3:
                reference = 0
            else:
                reference += 1
        else:
            newstring += s[i]
    return newstring
            

def alternatingSum(L):
    sum = 0
    flag = 0
    for i in L:
        sum += i * (-1) ** (flag % 2)
        flag += 1
    return sum

def median(L):
    newL = sorted(L)
    if len(L) == 0:
        return None
    elif len(L) % 2 == 1:
        return newL[int((len(L) - 1) / 2)]
    else:
        left = newL[int(len(L) / 2 - 1)]
        right = newL[int(len(L) / 2)]
        return (left + right) / 2
     
def isSorted(L):
    newL = list(L)
    ascend = sorted(newL)
    descend = sorted(newL, reverse=True)
    if newL == ascend or newL == descend:
        return True
    else:
        return False

def smallestDifference(L):
    if len(L) == 0:
        return -1
    smallest = 1000000000000
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            dis = abs(L[i] - L[j])
            if dis < smallest:
                smallest = dis
    return smallest

# Helper function to turn idx into the corredponding power
def index2power(length, idx):
    return length - 1 - idx

# Helper function to update the new list based on power
def updateList(l, power, multy):
    for i in range(len(l)):
        if index2power(len(l), i) == power:
            l[i] += multy
    return l

def multiplyPolynomials(p1, p2):
    length1 = len(p1)
    length2 = len(p2)
    newList = [0] * (length1 + length2 - 1)
    for i in range(length1):
        for j in range(length2):
            multy = p1[i] * p2[j]
            power = index2power(length1, i) + index2power(length2, j)
            newList = updateList(newList, power, multy)
    return newList

def lookAndSay(L):
    result = []
    i = 0
    while i < len(L):
        seg = 1
        j = i
        if j+1 == len(L): # First check whether we are in the last element
            result.append((seg, L[i]))
        else:
            while L[j] == L[j+1]:
                seg += 1
                j += 1
                # Second check whether we are in the last element
                if j+1 == len(L): 
                    break
            result.append((seg, L[i]))
        i = i + seg
    return result

def inverseLookAndSay(L):
    newList = []
    for i in L:
        for j in range(i[0]):
            newList.append(i[1])
    return newList

def nondestructiveRemoveRepeats(L):
    newL = []
    for i in L:
        if i not in newL:
            newL.append(i)
    return newL

def destructiveRemoveRepeats(L):
    newL = []
    idx = 0
    while idx < len(L):
        if L[idx] not in newL:
            newL.append(L[idx])
            idx += 1
        elif L[idx] in newL:
            L.pop(idx)

#################################################
# Test Functions
#################################################

def testGetAverage():
    print('Testing getAverage()...', end='')
    assert(getAverage('13,excused,14,absent') == 13.5)
    assert(getAverage('3,excused,4,absent,5') == 4)
    assert(getAverage('3,excused,4,absent,5,-123') == 4)
    assert(getAverage('a,b,0,c') == 0)
    assert(getAverage('a,b,c') == None)
    assert(getAverage('') == None)
    print('Passed!')

def testEncode():
    print('Testing encode()...', end='')
    assert(encode('cat') == 'AcBaCt')
    assert(encode('m3N4') == 'Am3BN4')
    assert(encode('qrstuv') == 'AqBrCsDtAuBv')
    assert(encode('x') == 'Ax')
    assert(encode('') == '')
    print('Passed!')
     
def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    print('Passed.')

def testMedian():
    print('Testing median()...', end='')
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    # now make sure this is non-destructive
    a = [ 2, 3, 2, 4, 2, 3]
    b = a + [ ]
    assert(almostEqual(median(b), 2.5))
    if (a != b):
        raise Exception('Your median() function should be non-destructive!')
    print('Passed')

def testIsSorted():
    print('Testing isSorted()...', end='')
    assert(isSorted([]) == True)
    assert(isSorted([1]) == True)
    assert(isSorted([1,1]) == True)
    assert(isSorted([1,2]) == True)
    assert(isSorted([2,1]) == True)
    assert(isSorted([2,2,2,2,2,1,1,1,1,0]) == True)
    assert(isSorted([1,1,1,1,2,2,2,2,3,3]) == True)
    assert(isSorted([1,2,1]) == False)
    assert(isSorted([1,1,2,1]) == False)
    assert(isSorted(range(10,30,3)) == True)
    assert(isSorted(range(30,10,-3)) == True)
    print('Passed!')

def testSmallestDifference():
    print('Testing smallestDifference()...', end='')
    assert(smallestDifference([]) == -1)
    assert(smallestDifference([2,3,5,9,9]) == 0)
    assert(smallestDifference([-2,-5,7,15]) == 3)
    assert(smallestDifference(list(range(0, 10**3, 5)) + [42]) == 2)
    print('Passed')

def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    # (2)*(3) == 6
    assert(multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert(multiplyPolynomials([2,-4],[3,5]) == [6,-2,-20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert(multiplyPolynomials([2,0,-4],[3,0,2,0]) == [6,0,-8,0,-8,0])
    print("Passed!")

def _verifyLookAndSayIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    lookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) ==  [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    assert(lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)])
    assert(lookAndSay([2]*5 + [5]*2) == [(5,2), (2,5)])
    assert(lookAndSay([5]*2 + [2]*5) == [(2,5), (5,2)])
    print("Passed!")

def _verifyInverseLookAndSayIsNondestructive():
    a = [(1,2), (2,3)]
    b = copy.copy(a)
    inverseLookAndSay(a) # ignore result, just checking for destructiveness here
    return (a == b)

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive() == True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    assert(inverseLookAndSay([(5,2), (2,5)]) == [2]*5 + [5]*2)
    assert(inverseLookAndSay([(2,5), (5,2)]) == [5]*2 + [2]*5)
    print("Passed!")

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

#################################################
# testAll and main
#################################################

def testAll():
    testGetAverage()
    testEncode()
    testAlternatingSum()
    testMedian()
    testIsSorted()
    testSmallestDifference()
    testMultiplyPolynomials()
    testLookAndSay()
    testInverseLookAndSay()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()

def main():
    cs112_f19_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
