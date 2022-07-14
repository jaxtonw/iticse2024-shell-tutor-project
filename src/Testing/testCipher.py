#!/usr/bin/env python

#                         ~
#                        (o)<  DuckieCorp Software License
#                   .____//
#                    \ <' )   Copyright (c) 2022 Erik Falor
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Permission is NOT granted, to any person who is NEITHER an employee NOR
# customer of DuckieCorp, to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS

import unittest
from main import cipherCharacter, cipherString

class TestCipher(unittest.TestCase):
    def testCipherCharAccuracyUppercase(self):
        upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        upperAlphabetShiftedOne = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedOne):
            cipherOutput = cipherCharacter(inputStr, 1)
            self.assertEquals(cipherOutput, expectedOutputStr)

        upperAlphabetShiftedFive = "FGHIJKLMNOPQRSTUVWXYZABCDE"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedFive):
            cipherOutput = cipherCharacter(inputStr, 5)
            self.assertEquals(cipherOutput, expectedOutputStr)

        upperAlphabetShiftedTen = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedTen):
            cipherOutput = cipherCharacter(inputStr, 10)
            self.assertEquals(cipherOutput, expectedOutputStr)

        upperAlphabetShiftedFifteen = "PQRSTUVWXYZABCDEFGHIJKLMNO"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedFifteen):
            cipherOutput = cipherCharacter(inputStr, 15)
            self.assertEquals(cipherOutput, expectedOutputStr)

        upperAlphabetShiftedTwenty = "UVWXYZABCDEFGHIJKLMNOPQRST"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedTwenty):
            cipherOutput = cipherCharacter(inputStr, 20)
            self.assertEquals(cipherOutput, expectedOutputStr)

        upperAlphabetShiftedTwentyFive = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        for inputStr, expectedOutputStr in zip(upperAlphabet, upperAlphabetShiftedTwentyFive):
            cipherOutput = cipherCharacter(inputStr, 25)
            self.assertEquals(cipherOutput, expectedOutputStr)

    def testCipherCharAccuracyLowercase(self):
        lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"

        lowerAlphabetShiftedOne = "bcdefghijklmnopqrstuvwxyza"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedOne):
            cipherOutput = cipherCharacter(inputStr, 1)
            self.assertEquals(cipherOutput, expectedOutputStr)

        lowerAlphabetShiftedFive = "fghijklmnopqrstuvwxyzabcde"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedFive):
            cipherOutput = cipherCharacter(inputStr, 5)
            self.assertEquals(cipherOutput, expectedOutputStr)

        lowerAlphabetShiftedTen = "klmnopqrstuvwxyzabcdefghij"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedTen):
            cipherOutput = cipherCharacter(inputStr, 10)
            self.assertEquals(cipherOutput, expectedOutputStr)

        lowerAlphabetShiftedFifteen = "pqrstuvwxyzabcdefghijklmno"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedFifteen):
            cipherOutput = cipherCharacter(inputStr, 15)
            self.assertEquals(cipherOutput, expectedOutputStr)

        lowerAlphabetShiftedTwenty = "uvwxyzabcdefghijklmnopqrst"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedTwenty):
            cipherOutput = cipherCharacter(inputStr, 20)
            self.assertEquals(cipherOutput, expectedOutputStr)

        lowerAlphabetShiftedTwentyFive = "zabcdefghijklmnopqrstuvwxy"
        for inputStr, expectedOutputStr in zip(lowerAlphabet, lowerAlphabetShiftedTwentyFive):
            cipherOutput = cipherCharacter(inputStr, 25)
            self.assertEquals(cipherOutput, expectedOutputStr)

    def testCipherCharAccuracyNoShift(self):
        upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for inputStr in upperAlphabet:
            cipherOutput = cipherCharacter(inputStr, 0)
            self.assertEquals(cipherOutput, inputStr)

        lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
        for inputStr in lowerAlphabet:
            cipherOutput = cipherCharacter(inputStr, 0)
            self.assertEquals(cipherOutput, inputStr)


    def testCipherCharIgnoreNonAlphabetic(self):
        testString = "./ !@#$%^&*()-_=`~<>~[]}{\n\t"
        for inputStr in testString:
            cipherOutput = cipherCharacter(inputStr, 1)
            self.assertEquals(cipherOutput, inputStr)
            cipherOutput = cipherCharacter(inputStr, 10)
            self.assertEquals(cipherOutput, inputStr)
            cipherOutput = cipherCharacter(inputStr, 20)
            self.assertEquals(cipherOutput, inputStr)

        numbers = "0123456789"
        for inputStr in numbers:
            cipherOutput = cipherCharacter(inputStr, 1)
            self.assertEquals(cipherOutput, inputStr)
            cipherOutput = cipherCharacter(inputStr, 10)
            self.assertEquals(cipherOutput, inputStr)
            cipherOutput = cipherCharacter(inputStr, 20)
            self.assertEquals(cipherOutput, inputStr)
    
    def testCipherStringAccuracyLowercase(self):
        lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
        lowerAlphabetShiftedOne = "bcdefghijklmnopqrstuvwxyza"
        self.assertEquals(cipherString(lowerAlphabet, 1), lowerAlphabetShiftedOne)

        lowerAlphabetShiftedFive = "fghijklmnopqrstuvwxyzabcde"
        self.assertEquals(cipherString(lowerAlphabet, 5), lowerAlphabetShiftedFive)

        lowerAlphabetShiftedTen = "klmnopqrstuvwxyzabcdefghij"
        self.assertEquals(cipherString(lowerAlphabet, 10), lowerAlphabetShiftedTen)

        lowerAlphabetShiftedFifteen = "pqrstuvwxyzabcdefghijklmno"
        self.assertEquals(cipherString(lowerAlphabet, 15), lowerAlphabetShiftedFifteen)

        lowerAlphabetShiftedTwenty = "uvwxyzabcdefghijklmnopqrst"
        self.assertEquals(cipherString(lowerAlphabet, 20), lowerAlphabetShiftedTwenty)

        lowerAlphabetShiftedTwentyFive = "zabcdefghijklmnopqrstuvwxy"
        self.assertEquals(cipherString(lowerAlphabet, 25), lowerAlphabetShiftedTwentyFive)

    def testCipherStringAccuracyUppercase(self):
        upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upperAlphabetShiftedOne = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
        self.assertEquals(cipherString(upperAlphabet, 1), upperAlphabetShiftedOne)

        upperAlphabetShiftedFive = "FGHIJKLMNOPQRSTUVWXYZABCDE"
        self.assertEquals(cipherString(upperAlphabet, 5), upperAlphabetShiftedFive)

        upperAlphabetShiftedTen = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
        self.assertEquals(cipherString(upperAlphabet, 10), upperAlphabetShiftedTen)

        upperAlphabetShiftedFifteen = "PQRSTUVWXYZABCDEFGHIJKLMNO"
        self.assertEquals(cipherString(upperAlphabet, 15), upperAlphabetShiftedFifteen)

        upperAlphabetShiftedTwenty = "UVWXYZABCDEFGHIJKLMNOPQRST"
        self.assertEquals(cipherString(upperAlphabet, 20), upperAlphabetShiftedTwenty)

        upperAlphabetShiftedTwentyFive = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        self.assertEquals(cipherString(upperAlphabet, 25), upperAlphabetShiftedTwentyFive)

    def testCipherStringIgnoreNonAlphabetic(self):
        testString = "./ !@#$%^&*()-_=`~<>~[]}{\n\t"
        cipherOutput = cipherString(testString, 0)
        self.assertEquals(cipherOutput, testString)
        cipherOutput = cipherString(testString, 1)
        self.assertEquals(cipherOutput, testString)
        cipherOutput = cipherString(testString, 10)
        self.assertEquals(cipherOutput, testString)
        cipherOutput = cipherString(testString, 20)
        self.assertEquals(cipherOutput, testString)

        numbers = "0123456789"
        cipherOutput = cipherString(numbers, 0)
        self.assertEquals(cipherOutput, numbers)
        cipherOutput = cipherString(numbers, 1)
        self.assertEquals(cipherOutput, numbers)
        cipherOutput = cipherString(numbers, 10)
        self.assertEquals(cipherOutput, numbers)
        cipherOutput = cipherString(numbers, 20)
        self.assertEquals(cipherOutput, numbers)

    def testCipherStringAccuracyMixedChars(self):
        testString = "L3t's pU5h TH!s 2 tHE L1m!t!"
        cipherOutput = cipherString(testString, 0)
        self.assertEquals(cipherOutput, testString)

        expectedOutputStr = "M3u't qV5i UI!t 2 uIF M1n!u!"
        cipherOutput = cipherString(testString, 1)
        self.assertEquals(cipherOutput, expectedOutputStr)

        expectedOutputStr = "Q3y'x uZ5m YM!x 2 yMJ Q1r!y!"
        cipherOutput = cipherString(testString, 5)
        self.assertEquals(cipherOutput, expectedOutputStr)

        expectedOutputStr = "V3d'c zE5r DR!c 2 dRO V1w!d!"
        cipherOutput = cipherString(testString, 10)
        self.assertEquals(cipherOutput, expectedOutputStr)

        expectedOutputStr = "A3i'h eJ5w IW!h 2 iWT A1b!i!"
        cipherOutput = cipherString(testString, 15)
        self.assertEquals(cipherOutput, expectedOutputStr)

        expectedOutputStr = "F3n'm jO5b NB!m 2 nBY F1g!n!"
        cipherOutput = cipherString(testString, 20)
        self.assertEquals(cipherOutput, expectedOutputStr)

        expectedOutputStr = "K3s'r oT5g SG!r 2 sGD K1l!s!"
        cipherOutput = cipherString(testString, 25)
        self.assertEquals(cipherOutput, expectedOutputStr)


if __name__ == "__main__":
    unittest.main()
