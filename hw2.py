#################################################
# hw2.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f19_week2_linter
import math
from tkinter import *
import random

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

def integral(f, a, b, N):
    width = (b - a) / N
    estimate = 0
    i = a 
    while almostEqual(i, b) == False:
        estimate += f(i) + f(i + width)
        i += width
    return estimate * width / 2

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        max = int(math.sqrt(n))
        for i in range(3, max + 1, 2):
            if n % i == 0:
                return False
        return True

def getKthDigit(n, k):
    n = int(n / 10 ** k)
    return abs(n) % 10

def getDigitSum(n):
    sum_n = 0
    while n != 0:
        sum_n += n % 10
        n //= 10
    return sum_n

def isSmith(n):
    if isPrime(n):
        return False
    else:
        prime_n = 0
        n_copy = n
        while n != 1:
            for i in range(2, n_copy + 1):
                if isPrime(i) & (n % i == 0):
                    prime_n += getDigitSum(i)
                    n /= i
        if prime_n == getDigitSum(n_copy):
            return True
        else:
            return False
                
def nthSmithNumber(n):
    i = 4
    count = -1
    while count != n:
        if isSmith(i):
            count += 1
        i += 1
    return i - 1        

def drawPattern1(points, canvas, width, height):
    pass

def drawPattern2(points, canvas, width, height):
    pass

def drawPattern3(points, canvas, width, height):
    pass

def drawPattern4(canvas, width, height):
    pass

def playPig():
    print('Not yet implemented!')

#################################################
# Bonus/Optional functions for you to write
#################################################
def makeBoard(moves):
    sum = 0
    for i in range(moves):
        sum += 8 * 10 ** i
    return sum

def digitCount(n):
    n = abs(n)
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

def kthDigit(n, k):
    n = int(n / 10 ** k)
    return abs(n) % 10

def replaceKthDigit(n, k, d):
    left, right = 0, 0
    for i in range(k):
        right += kthDigit(n, i) * (10 ** i)
    if k >= digitCount(n):
        left = d * 10 ** k
    else:
        for i in range(k+1, digitCount(n)):
            left += kthDigit(n, i) * (10 ** i)
        left += d * 10 ** k
    return left + right
    
def getLeftmostDigit(n):
    return n // 10 ** (digitCount(n) - 1)

def clearLeftmostDigit(n):
    return n - getLeftmostDigit(n) * (10 ** (digitCount(n)-1))

def makeMove(board, position, move):
    if move != 1 and move != 2:
        return("move must be 1 or 2!")
    elif position > digitCount(board):
        return("offboard!")
    elif kthDigit(board, digitCount(board)-position) != 8:
        return("occupied!")
    else:
        return replaceKthDigit(board, digitCount(board)-position, move)
        
def isWin(board):
    count = 0
    for i in range(digitCount(board)):
        if kthDigit(board, i) == 1 or kthDigit(board, i) == 8:
            continue
        else:
            count += 1
            if kthDigit(board, i+1) == 1 and kthDigit(board, i+2) == 1:
                return True
            else:
                continue
    return False

def isFull(board):
    for i in range(digitCount(board)):
        if kthDigit(board, i) == 8:
            return False
    return True
        
def bonusPlay112(game):
    board = makeBoard(getLeftmostDigit(game))
    game = clearLeftmostDigit(game)
    player_count = 0
    for i in range(digitCount(game), 0, -2):
        position = kthDigit(game, i - 1)
        move = kthDigit(game, i - 2)
        result = makeMove(board, position, move)
        player_count += 1
        if player_count % 2 == 1:
            if result == "move must be 1 or 2!":
                return("%d: Player 1: %s" % (board, result))
            elif result == "offboard!":
                return("%d: Player 1: %s" % (board, result))
            elif result == "occupied!":
                return("%d: Player 1: %s" % (board, result))
            elif isWin(result):
                return("%d: Player 1 wins!" % result)
            elif isFull(result):
                return("%d: Tie!" % result)
            else:
                board = result
                
        else:
            if result == "move must be 1 or 2!":
                return("%d: Player 2: %s" % (board, result))
            elif result == "offboard!":
                return("%d: Player 2: %s" % (board, result))
            elif result == "occupied!":

                return("%d: Player 2: %s" % (board, result))
            elif isWin(result):
                return("%d: Player 2 wins!" % result)
            elif isFull(result):
                return("%d: Tie!" % result)
            else:
                board = result
        
    return("%d: Unfinished!" % board)

def carrylessAdd(x1, x2):
    length_x1 = digitCount(x1)
    length_x2 = digitCount(x2)
    length = max(length_x1, length_x2)
    sum = 0
    for i in range(length):
        digit_x1 = kthDigit(x1, i)
        digit_x2 = kthDigit(x2, i)
        sum += kthDigit(digit_x1+digit_x2, 0) * 10 ** i
    return sum

def bonusCarrylessMultiply(x1, x2):
    length = digitCount(x2)
    multy = 0
    for i in range(length):
        times = kthDigit(x2, i)
        temp = 0
        for j in range(times):
            temp = carrylessAdd(temp, x1)
        multy = carrylessAdd(multy, temp * 10 ** i)
    return multy

#################################################
# Test Functions
#################################################

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assert(almostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon))
    assert(almostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon))
    assert(almostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon))
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assert(nthSmithNumber(0) == 4)
    assert(nthSmithNumber(1) == 22)
    assert(nthSmithNumber(2) == 27)
    assert(nthSmithNumber(3) == 58)
    assert(nthSmithNumber(4) == 85)
    assert(nthSmithNumber(5) == 94)
    print('Passed.')

def runDrawPattern1(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern1(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern2(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern2(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern3(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern3(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern4(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern4(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawPatterns():
    print('** Note: You need to manually test drawPatterns()')
    print('Calling runDrawPattern1(5, 400, 400):')
    runDrawPattern1(5, 400, 400)
    print('Calling runDrawPattern1(10, 800, 400):')
    runDrawPattern1(10, 800, 400)
    print('Calling runDrawPattern2(5, 400, 400):')
    runDrawPattern2(5, 400, 400)
    print('runDrawPattern2(10, 800, 400):')
    runDrawPattern2(10, 800, 400)
    print('runDrawPattern3(5, 400, 400):')
    runDrawPattern3(5, 400, 400)
    print('runDrawPattern3(10, 800, 400)')
    runDrawPattern3(10, 800, 400)
    print('runDrawPattern4(600, 600)')
    runDrawPattern4(600, 600)

def testPlayPig():
    print('** Note: You need to manually test playPig()')

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testreplaceKthDigit():
    print("Testing replaceKthDigit()...", end="")
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    assert(clearLeftmostDigit(60789) == 789)
    print("Passed!")

def testBonusPlay112():
    print("Testing bonusPlay112()... ", end="")
    assert(bonusPlay112( 5 ) == "88888: Unfinished!")
    assert(bonusPlay112( 521 ) == "81888: Unfinished!")
    assert(bonusPlay112( 52112 ) == "21888: Unfinished!")
    assert(bonusPlay112( 5211231 ) == "21188: Unfinished!")
    assert(bonusPlay112( 521123142 ) == "21128: Player 2 wins!")
    assert(bonusPlay112( 521123151 ) == "21181: Unfinished!")
    assert(bonusPlay112( 52112315142 ) == "21121: Player 1 wins!")
    assert(bonusPlay112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(bonusPlay112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(bonusPlay112( 51211 ) == "28888: Player 2: occupied!")
    assert(bonusPlay112( 5122221 ) == "22888: Player 1: occupied!")
    assert(bonusPlay112( 51261 ) == "28888: Player 2: offboard!")
    assert(bonusPlay112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():

    testIntegral()
    testNthSmithNumber()
    testreplaceKthDigit()
#    testDrawPatterns()
#    testPlayPig()
    testBonusPlay112()
    testBonusCarrylessMultiply()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
