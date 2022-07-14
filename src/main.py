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

import sys
from typing import Optional


def printUsage(exitCode : int = 0) -> None:
    MSG = f"""\
    USAGE:
      $ python {sys.argv[0]} <file_path> [rotation_distance]
    
      The <file_path> argument is *required* and must be a path to a valid file.

      The rotation distance argument is *optional*, and is integers in the range
        0 to 25, inclusive. If a rotation distance is not specified, all rotation
        distances are run and output.
    """
    print(MSG, end='')
    sys.exit(exitCode)


def printBanner(filename : str, rotation : int) -> None:
    MSG = f"""\
======================================================
{filename} rotated by {rotation} positions
======================================================
"""
    print(MSG, end='')


def processFile(filename : str, rotation : Optional[int]) -> None:
    file = open(filename)
    fileContents = file.read()
    file.close()
    if rotation is None:
        # Do all rotations
        for rot in range(0, 25):
            printBanner(filename, rot)
            cipherText = cipherString(fileContents, rot)
            print(cipherText, end='')
    else:
        printBanner(filename, rotation)
        cipherText = cipherString(fileContents, rotation)
        print(cipherText, end='')


def cipherString(stringToCipher : str, rotation : int) -> str:
    cipheredMessage = ""
    for character in stringToCipher:
        cipheredMessage += cipherCharacter(character, rotation)
    return cipheredMessage


def cipherCharacter(char : str, rot : str) -> str:
    charOrdVal = ord(char)
    if 65 <= charOrdVal < 90:
        charBaseVal = ord("A")
    elif 97 < charOrdVal < 122:
        charBaseVal = ord("a")
    else:
        # Don't cipher this character
        return char
    # Subtract base value from original ord value so we can perform modular arithmetic
    newCharOrdVal = (charOrdVal - charBaseVal)
    # Add rotation value
    newCharOrdVal += rot
    # mod 26 to 'shift' correctly shift around alphabet
    newCharOrdVal = newCharOrdVal % 26
    # Shift the newCharOrdVal by the charBaseVal to return to the 'true' ordinal value
    newCharOrdVal = newCharOrdVal + charBaseVal
    # Convert ordinal value back to character to return
    return chr(newCharOrdVal)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usageMessage(exitCode=0)
    if len(sys.argv) == 2:
        # Only the filename is provided, so do all rotations
        rotationDist = None
    else:
        rotationDist = sys.argv[2]
        if rotationDist.isdigit():
            rotationDist = int(rotationDist)
        else:
            print(f"ERROR: '{rotationDist}' is not a valid rotation distance\n")
            usageMessage(exitCode=1)
        if rotationDist < 0 or rotationDist > 25:
            print(f"ERROR: '{rotationDist}' is not in the inclusive range of [0, 25]\n")
            usageMessage(exitCode=1)
    filename = sys.argv[1]
    processFile(filename=filename, rotation=rotationDist)