#################################################
# hw1.py
#
# Your name:
# Your andrew id:jiaxuanz
#################################################

import cs112_f19_week1_linter
import math

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

def nearestOdd(n):
    if n % 2 == 0:
        return n - 1 
    n = int(n)
    if n % 2 != 0:
            return n
    if n >= 0:
        return n + 1
    else:
        return n - 1

def isPerfectSquare(n):
    if (isinstance(n, int) == False) or (n < 0):
        return False
    else:
        if int(math.sqrt(n)) ** 2 == n:
            return True
        else:
            return False

def numberOfPoolBalls(rows):
    return (rows + 1) * rows / 2

def numberOfPoolBallRows(balls):
    
    return 42

def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > midpoints + 1 or midpoints < 0:
        return None
    else:
        Red1 = rgb1 // 1000000  
        Red2 = rgb2 // 1000000
        Green1 = (rgb1 - Red1 * 1000000) // 1000
        Green2 = (rgb2 - Red2 * 1000000) // 1000
        Blue1 = rgb1 - Red1 * 1000000 - Green1 * 1000
        Blue2 = rgb2 - Red2 * 1000000 - Green2 * 1000
        redGap = (Red1 - Red2) / (midpoints + 1)
        greenGap = (Green1 - Green2) / (midpoints + 1)
        blueGap = (Blue1 - Blue2) / (midpoints + 1)
        Red3 = roundHalfUp(Red1 - n * redGap)
        Green3 = roundHalfUp(Green1 - n * greenGap)
        Blue3 = roundHalfUp(Blue1 - n * blueGap)
        return Red3 * 1000000 + Green3 * 1000 + Blue3

#################################################
# Bonus/Optional functions for you to write
#################################################

from writing_session1_practice import getKthDigit

def handToDice(hand):
    return getKthDigit(hand,2), getKthDigit(hand,1), getKthDigit(hand,0)

def diceToOrderedHand(a, b, c):
    if a == max(a,b,c):
        temp = max(b,c)
    elif b == max(a,b,c):
        temp = max(a,c)
    else:
        temp = max(a,b)
    return max(a,b,c) * 100 + temp * 10 + min(a,b,c)
    
def playStep2(hand, dice):
    a, b, c = handToDice(hand)
    hand = diceToOrderedHand(a, b, c)
    left = getKthDigit(hand,2)
    middle = getKthDigit(hand,1)
    right = getKthDigit(hand,0)
    if left == middle and middle != right: # pair
        right = getKthDigit(dice, 0)
        return diceToOrderedHand(left, middle, right), dice // 10
    elif left == right and middle != right:
        middle = getKthDigit(dice, 0)
        return diceToOrderedHand(left, middle, right), dice // 10
    elif middle == right and left != right:
        left = getKthDigit(dice, 0)
        return diceToOrderedHand(left, middle, right), dice // 10
    elif left == middle and middle == right:
        return hand, dice
    else:
        middle = getKthDigit(dice, 0)
        right = getKthDigit(dice, 1)
        return diceToOrderedHand(left, middle, right), dice // 100
    
def score(hand):
    left = getKthDigit(hand,2)
    middle = getKthDigit(hand,1)
    right = getKthDigit(hand,0)
    if left == middle and middle != right:
        return 10 + left + middle
    elif left == right and middle != right:
        return 10 + left + right
    elif middle == right and right != left:
        return 10 + middle + right
    elif left == middle and middle == right:
        return 20 + left + middle + right
    else:
        return left

def bonusPlayThreeDiceYahtzee(dice):
    hand = getKthDigit(dice,2) * 100 \
    + getKthDigit(dice,1) * 10 + getKthDigit(dice,0)
    dice = getKthDigit(dice,6) * 1000 \
    + getKthDigit(dice,5) * 100 + getKthDigit(dice,4) * 10 + getKthDigit(dice,3)
    hand, dice = playStep2(hand, dice)
    hand, dice = playStep2(hand, dice)
    return hand, score(hand)

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Test Functions
#################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed.')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
#    testNearestOdd()
#    testIsPerfectSquare()
#    testNumberOfPoolBalls()
#    testNumberOfPoolBallRows()
#    testColorBlender()
     testBonusPlayThreeDiceYahtzee()
    # testBonusFindIntRootsOfCubic()

def main():
    cs112_f19_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
