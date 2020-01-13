#################################################
# writing_session3_practice_solutions.py
#################################################

import cs112_f19_week3_linter
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

#################################################
# Functions for you to write
#################################################

def isTenly(n):
    sum = 0
    for i in range(len(str(n))):
        sum += (n % 10)
        n //= 10 
    return sum == 10

def nthTenlyPrime(n):
    count = 0
    found = 0
    while found != n:
        if isPrime(count) and isTenly(count):
            found += 1
        count += 1
    return count - 1

def rotateString(s, k):
    if k >= 0:
        while k > len(s):
            k -= len(s)
        left = s[0:k]
        right = s[k:]
    elif k < 0:
        while abs(k) > len(s):
            k += len(s)
        left = s[0:len(s)-abs(k)]
        right = s[k:]
    return right + left

def shiftLetter(letter, shift):
    if shift >= 0:
        if ord(letter) <= 90:
            if ord(letter) + shift <= 90:
                return chr(ord(letter)+shift)
            else:
                return chr(64 + (shift - (90 - ord(letter))))
        elif ord(letter) <= 122:
            if ord(letter) + shift <= 122:
                return chr(ord(letter)+shift)
            else:
                return chr(96 + (shift - (122 - ord(letter))))
    else:
        if ord(letter) <= 90:
            if ord(letter) + shift >= 65:
                return chr(ord(letter)+shift)
            else:
                return chr(91 + (shift + (ord(letter) - 65)))
        elif ord(letter) <= 122:
            if ord(letter) + shift >= 97:
                return chr(ord(letter)+shift)
            else:
                return chr(123 + (shift + (ord(letter) - 97)))

def applyCaesarCipher(message, shift):
    result = ''
    for i in message:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            result += shiftLetter(i, shift)
        else:
            result += i
    return result

def hasBalancedParentheses(s):
    while s.find("()") != -1:
        s = s.replace("()", "")
    if s == "":
        return True
    else:
        return False

def largestNumber(s):
    result = 0
    for i in range(len(s)):
        length = 0
        while (i+length<len(s)) and ord(s[i+length]) >= 48 \
        and ord(s[i+length]) <= 57:
            length += 1
        if length > 0 and int(s[i:i+length]) > result:
            result = int(s[i:i+length])
        else:
            continue
    if result != 0:
        return result
    else:
        return None

def longestSubpalindrome(s):
    result = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(result):
                    result = s[i:j]
                elif len(s[i:j]) == len(result):
                    if s[i:j] > result:
                        result = s[i:j]
    if result != " ":
        return result
    else:
        return None

import string
def collapseWhitespace(s):
    newstring = ""
    flag = 0
    for i in s:
        if i in string.whitespace and flag == 0:
            newstring += " " 
            flag += 1
        elif i not in string.whitespace and flag == 1:
            newstring += i
            flag -= 1
        elif i not in string.whitespace and flag == 0:
            newstring += i
    return newstring

def topScorer(data):
    if data == "":
        return None
    topScore = 0
    topPlayer = ""
    data = data.split("\n")
    for line in data:
        record = line.split(",")
        currentScore = 0
        for i in range(1, len(record)):
            currentScore += int(record[i])
        if currentScore > topScore:
            topScore, topPlayer = currentScore, record[0]
        elif currentScore == topScore:
            topPlayer += (",%s" % record[0])

    return topPlayer
            
def drawFlagOfQatar(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw Flag of Qatar>')

def drawFlagOfTheEU(canvas, width, height):
    canvas.create_text(width/2, height/2, text='<TBD: Draw Flag of the EU>')

#################################################
# Test Functions
#################################################

def testnthTenlyPrime():
    print("Testing nthTenlyPrime()...", end="")
    assert(nthTenlyPrime(1) == 19)
    assert(nthTenlyPrime(2) == 37)
    assert(nthTenlyPrime(3) == 73)
    assert(nthTenlyPrime(4) == 109)
    assert(nthTenlyPrime(5) == 127)
    print("Passed!")
    
def testRotateString():
    print("Testing rotateString()...", end="")
    assert(rotateString("abcde", 0) == "abcde")
    assert(rotateString("abcde", 1) == "bcdea")
    assert(rotateString("abcde", 2) == "cdeab")
    assert(rotateString("abcde", 3) == "deabc")
    assert(rotateString("abcde", 4) == "eabcd")
    assert(rotateString("abcde", 5) == "abcde")
    assert(rotateString("abcde", 25) == "abcde")
    assert(rotateString("abcde", 28) == "deabc")
    assert(rotateString("abcde", -1) == "eabcd")
    assert(rotateString("abcde", -2) == "deabc")
    assert(rotateString("abcde", -3) == "cdeab")
    assert(rotateString("abcde", -4) == "bcdea")
    assert(rotateString("abcde", -5) == "abcde")
    assert(rotateString("abcde", -25) == "abcde")
    assert(rotateString("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
                             "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
                             "zabcdefghijklmnopqrstuvwxy")
    assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed.")

def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert(hasBalancedParentheses("()") == True)
    assert(hasBalancedParentheses("") == True)
    assert(hasBalancedParentheses("())") == False)
    assert(hasBalancedParentheses("()(") == False) 
    assert(hasBalancedParentheses(")(") == False)
    assert(hasBalancedParentheses("(()())") == True)
    assert(hasBalancedParentheses("((()())(()(()())))") == True)
    assert(hasBalancedParentheses("((()())(()((()())))") == False)
    assert(hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    print("Passed!")

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def runDrawFlagOfQatar(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfQatar(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawFlagOfQatar():
    print('Calling runDrawFlagOfQatar(400, 400):')
    runDrawFlagOfQatar(400, 400)
    print('Calling runDrawFlagOfQatar(800, 400):')
    runDrawFlagOfQatar(800, 400)

def runDrawFlagOfTheEU(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawFlagOfTheEU(canvas, width, height)
    root.mainloop()
    print("bye!")

def testDrawFlagOfTheEU():
    print('Calling runDrawFlagOfTheEU(400, 400):')
    runDrawFlagOfTheEU(400, 400)
    print('Calling runDrawFlagOfTheEU(800, 400):')
    runDrawFlagOfTheEU(800, 400)

#################################################
# testAll and main
#################################################

def testAll():
    testnthTenlyPrime()
    testRotateString()
    testApplyCaesarCipher()
    testHasBalancedParentheses()
    testLargestNumber()
    testLongestSubpalindrome()
    testCollapseWhitespace()
    testTopScorer()
#    testDrawFlagOfQatar()
#    testDrawFlagOfTheEU()

def main():
    cs112_f19_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
