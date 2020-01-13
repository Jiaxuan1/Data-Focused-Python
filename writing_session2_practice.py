#################################################
# writing_session2_practice.py
#################################################

import cs112_f19_week2_linter
import math
from tkinter import *

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

def digitCount(n):
    digit = 1
    while True:
        if abs(n / (10 ** digit)) <= 1:
            return digit
        else:
            digit += 1

def gcd(a,b):
    while b != 0:
        copy_b = b
        b = a % b
        a = copy_b
    return a

def hasConsecutiveDigits(n):
    n = abs(n)
    last_digit = -1 
    for i in range(digitCount(n)):
        current_digit = n % 10
        n //= 10
        if current_digit == last_digit:
            return True
        else:
            last_digit = current_digit
    return False

def mostFrequentDigit(n): # have better solution??
#    0_count, 1_count, 2_count, 3_count, 4_count = 0, 0, 0, 0, 0
#    5_count, 6_count, 7_count, 8_count, 9_count = 0, 0, 0, 0, 0
#    for i in range(digitCount(n)):
#        digit = n % 10
#        if digit == 0:
#            0_count += 1
#        elif digit == 1:
#            1_count += 1
    return 42

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = int(math.sqrt(n))
    for i in range(3, max + 1, 2):
        if n % i == 0:
            return False
    return True

def getKthDigit(n, k):
    n = int(n / 10 ** k)
    return abs(n) % 10

def nthAdditivePrime(n):
    number = 2
    i = 0
    while i <= n:
        if isPrime(number) == False:
            number += 1
            continue
        else:
            length = digitCount(number)
            sum = 0
            copy_number = number
            for j in range(length):
                digit = copy_number % 10
                sum += digit
                copy_number //= 10
            if isPrime(sum):
                i += 1
            number += 1
    return number - 1

def nthPalindromicPrime(n):
    number = 2
    i = 0
    while i <= n:
        if isPrime(number) == False:
            number += 1
            continue
        else:
            length = digitCount(number)
            sum = 0
            copy_number = number
            for j in range(length):
                digit = copy_number % 10
                sum += (digit * (10 ** (length - 1 - j)))
                copy_number //= 10
            if sum == number:
                i += 1
            number += 1
    return number - 1

def isRotation(x, y):
    length_y = digitCount(y)
    length_x = digitCount(x)
    gap = -1
    if length_y != length_x:
        return False
    else:
        digit_y = getKthDigit(y, 0)
        for i in range(length_x):
            digit = getKthDigit(x, i)
            if digit == digit_y:
                gap = i
        if gap == -1:
            return False
        for j in range(length_y):
            digit = getKthDigit(y, j)
            if j + gap >= length_y:
                if digit == getKthDigit(x, gap - (length_x - j)):
                    continue
                else:
                    return False
            else:
                if digit == getKthDigit(x, j + gap):
                    continue
                else:
                    return False
        return True

def findZeroWithBisection(f, x0, x1, epsilon):
    while (x1 - x0) >= epsilon:
        mid = (x0 + x1) / 2
        if almostEqual(f(mid), 0, epsilon):
            return mid
        elif f(mid) * f(x0) < 0:
            x1 = mid
        elif f(mid) * f(x1) < 0:
            x0 = mid
    return (x0 + x1) / 2

def carrylessAdd(x1, x2):
    length_x1 = digitCount(x1)
    length_x2 = digitCount(x2)
    length = max(length_x1, length_x2)
    sum = 0
    for i in range(length):
        digit_x1 = getKthDigit(x1, i)
        digit_x2 = getKthDigit(x2, i)
        sum += getKthDigit(digit_x1+digit_x2, 0) * 10 ** i
    return sum

def drawDashedLine(dashLength, canvas, width, height):
    pass

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed.')

def testGcd():
    print('Testing gcd()...', end='')
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert (gcd(2*3*4*5,3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assert(gcd(x, y) == g)
    print('Passed.')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed.')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed.')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assert(nthAdditivePrime(0) == 2)
    assert(nthAdditivePrime(1) == 3)
    assert(nthAdditivePrime(5) == 23)
    assert(nthAdditivePrime(10) == 61)
    assert(nthAdditivePrime(15) == 113)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assert(isRotation(1, 1) == True)
    assert(isRotation(1234, 4123) == True)
    assert(isRotation(1234, 3412) == True)
    assert(isRotation(1234, 2341) == True)
    assert(isRotation(1234, 1234) == True)
    assert(isRotation(1234, 123) == False)
    assert(isRotation(1234, 12345) == False)
    assert(isRotation(1234, 1235) == False)
    assert(isRotation(1234, 1243) == False)
    print('Passed.')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

def runDrawDashedLine(dashLength, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawDashedLine(dashLength, canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawDashedLine():
    print('Calling runDrawDashedLine(5, 400, 400):')
    runDrawDashedLine(5, 400, 400)
    print('Calling runDrawDashedLine(20, 800, 400):')
    runDrawDashedLine(20, 800, 400)

#################################################
# testAll and main
#################################################

def testAll():
    testDigitCount()
    testGcd()   
    testHasConsecutiveDigits()  
#    testMostFrequentDigit()
    testNthAdditivePrime()   
    testNthPalindromicPrime()
    testIsRotation()
    testFindZeroWithBisection()
    testCarrylessAdd()
#    testDrawDashedLine()

def main():
    cs112_f19_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
