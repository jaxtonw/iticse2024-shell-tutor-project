# Software Development Plan

## Phase 0: Requirements Specification

### What Am I Asked To Do? 
This project will be a Python "Caesar Cipher" program. It will take command line arguments that specify the file to cipher/decipher, and an argument specifying the rotation distance. If this argument is not provided, then all valid rotation distances will be output.

The Caesar Cipher is a speicific cipher algorithm that shifts alphabetic characters, and will "wrap around" the alphabet. For example, with a cipher rotation of 1, the letter A will become B, the letter B becomes C, the letter Z becomes A, so on and so forth. Uppercase characters will remain upppercase, and lowercase characters will remain lowercase. Characters that are not alphabetic, meaning A-Z, will remain untouched by the Caesar Cipher. 

If given *no* arguments on the command line, this program will also output a usage message dictating how to use it. If invalid arguments are provided (namely, if the rotation distance is not in the inclusive range of 0-25), a message indicating an invalid rotation distance was specified is printed out *as well as* the usage message.

Unit tests are also going to be created, as I have a proclivity to do test driven development. This isn't directly required by the instructions, but is something I desire to do to ensure the program is robust and accurate in it's output.

### Things I Do Know
Luckily, I've been working with Python for a while now and feel confident that I know *most* of the operations that I will need to perform to complete this program. I feel confident with modular arithmetic (to shift characters). I feel confident with crafting a usage message. I feel *mostly* confident with creating unittests using the `unittest` framework.

### Things I Don't Know/Should Research More
*   I should research processing command line arguments a bit more. I recall it has something to do with `sys.argv`, but it's always good to have a refresher.
*   Reading files and processing them line-by-line is something I do know, but I should definitely see if there might be a better way than what I've been taught
*   Double check that the `open` function behaves as I recall
    *   To close a file, do I use a `close` function, or a `close` method on the file object?
    *   Is there a better way to read the file than the `file.readline()` method?
*   I need to freshen up on `ord` and `chr` functions
    *   I definitely need to know the `ord` values of characters in the ranges `[A-Z]` and `[a-z]` so I can devise an algorithm to "shift" them. I hope their `ord` values are sequential!
*   A refresher on setting up `unittest`s will be beneficial, even though I've worked with it before and feel *mostly* confident with it
    *   What are some of the key `assert` methods that will come in handy?
    *   Did the starter code handle most of the `unittest` setup for me with `runTests.py`, or do I need to do anything else?
  
## Phase 1: System Analysis

### Program Input
This program takes command line arguments to receive input of the filename and rotation distance.

If the file exists, it's contents are read in as a string and processed by the program. This file will likely be processed line-by-line, as I have a proclivity to process files this way.

### Applying Cipher Algorithm
When reading a string and applying the Caesar Cipher to it, apply the cipher algorithm *only* to characters that are in the range `[A-Z]` and `[a-z]`. If a character does not fall into this range, we do *not* apply the cipher to it. Characters that are *not* shifted are appended to the `outputString` as is, and characters that do get shifted get inputted into a "shift" function, and it's result is appended to the `outputString`.

### Caesar Cipher Shift Character Algorithm
One of the key "algorithms" I need to shift the characters is going to rely on modular arithmetic. As I have 26 characters to "wrap" around the alphabet, I am going to want to use `mod 26` (written as `% 26` in Python) to compute the "shift" of characters. To be more detailed, I want to do the following:
    Find the `ord` value of `A` (or `a`, if shifting a lowercase character)
    Find the `ord` value of the character being shifted
    Subtract `ord` value of `A` (or `a`) from the `ord` value of the character being shifted
    Add the rotation distance to this subtracted value
    `mod 26` the new value, store it
    Add back the value of `A` (or `a`) to this new value
    Use the `chr` function to convert this value back into a character

### Program Output
The `outputString` is printed out after applying the cipher to the original string.

### Unit Testing
I have mentioned this before, but I'm going to use the `unittest` framework to setup unit tests. I will craft a test suite that can be run from the test driver program `runTests.py` using the built in `assert` methods on a `unittest` Test Suite.

## Phase 2: Design

This program should be relatively straight forward. However, I've found a few key attributes that can be separated and likely turned into functions.

0.  Parse command line arguments
    *   Read from `sys.argv` and determine what to do from there
    *   If no args are provided, or arguments are invalid, print the usage message
        *   If args aren't provided, just print usage message and exit with a success exit code (exit code 0, if you know shell conventions)
        *   If arguments are invalid (namely, if the rot distance isn't an integer in range 0-25), print message indicating the argument is invalid and then print a usage message, exiting with a failure exit code (exit code not equal to 0, if you know shell conventions. I'll probably use exit code 1)
1.  Usage message
    *   Prints the usage message and then exits the program with a specified exit code
2.  Process file
    *   Given a filename argument, open and read the file into a string, and then apply the cipher to the string
    *   Can take an argument that specifies the specific rotation distance. If this argument is None, then print all rotation distances 0-25
    *   Prints the banner indicating the rotation distance
    *   Gives the string and rotation distance to the actual `cipherString` function, printing the result
    *   Kind of the main "driver" of the program
3.  Print banner
    *   Prints the banner with a specified rotation distance
    *   The banner is the same, aside from the number of the rotation distance, so this is perfect for a small function!
4.  Cipher string
    *   Given a string and rotation distance, cipher the string with the Caesar Cipher
    *   Relies on cipher character function to cipher individual characters 
    *   Return the newly constructed ciphered string
5.  Cipher character
    *   Takes a single character and rotation distance
    *   Returns the newly ciphered character
    *   If given a character that shouldn't be ciphered, return that character as-is

### Function Psuedocode
The psuedocode for these function stubs are going to use Python-isms, but won't necessarily be working Python code. It will be *very* similar though, because Python is basically "executable psuedocode" by design. 

I like Python's type hinting syntax, so I use it for function arguments and return types.

#### Parse Command Line Arguments
Parse the command line arguments correctly, continuing on to cipher message or print usage message and exit

Returns nothing

```py
def parseCLArgs() -> None:
    if len of sys.argv is 1:
        usageMessage(exitCode=0)
    if len of sys.argv is 2:
        # Only the filename is provided, so do all rotations
        rotationDist = None
    else:
        rotationDist = sys.argv[2]
        if rotationDist is an integer:
            rotationDist = int(rotationDist)
        else:
            print(f"ERROR: {rotationDist} is not a valid rotation distance\n")
            usageMessage(exitCode=1)
        if rotationDist < 0 or rotationDist > 25:
            print(f"ERROR: {rotationDist} is not in the inclusive range of [0, 25]\n")
            usageMessage(exitCode=1)
    filename = sys.argv[1]
    processFile(filename=filename, rotation=rotationDist)
```

*   Notes
    *   `sys.argv[0]` is the main filename, so `len(sys.argv) > 1` always
    *   If `rotationDist` is `None`, that indicates all rotations will be done by `processFile`
    *   This likely won't be an actual function, and will just be 

#### Usage Message
Print a usage message, exiting with exitCode

Doesn't return anything, as program terminates in this function

```py
def printUsage(exitCode : int = 0) -> None:
    MSG =
    f"""
    USAGE:
      $ python {sys.argv[0]} <file_path> [rotation_distance]
    
      The <file_path> argument is *required* and must be a path to a valid file.

      The rotation distance argument is *optional*, and is integers in the range
        0 to 25, inclusive. If a rotation distance is not specified, all rotation
        distances are run and output.
    """
    print(MSG) without newline at end
    exit with exitCode
```

*   Notes
    *   `sys.argv[0]` is the file name, so it can be used to provide an accurate filename in the usage message printed

#### Process File
Given a filename and rotation distance, open and read the file into a string, and then apply the cipher to the string

Returns nothing

```py
def processFile(filename : str, rotation : Optional[int]) -> None:
    file = open(filename)
    fileContents = file.read()
    file.close()
    if rotation is None:
        # Do all rotations
        for rot in 0 to 25:
            printBanner(filename, rot)
            cipherText = cipherString(fileContents, rot)
            print(cipherText) with no extra newline
    else:
        printBanner(filename, rotation)
        cipherText = cipherString(fileContents, rotation)
        print(cipherText) with no extra newline
```

*   Notes
    *   `open` function will crash if `filename` is not a valid file for reading; this is expected and relied on
    *   The `Optional[int]` type indicates a value can be `None` or an `int`
    *   Checking for `rotation` being in [0, 25] is done before this function is called 

#### Print Banner
Prints the banner with a specified rotation distance

Returns nothing, just prints the banner

```py
def printBanner(filename : str, rotation : int) -> None:
    MSG =
    f"""
    ======================================================
    {filename} rotated by {rotation} positions
    ======================================================
    """
    print(MSG) with no extra newline
```

#### Cipher String
Given a string and rotation distance, cipher the string with the Caesar Cipher

Returns the string after it's been ciphered

```py
def cipherString(stringToCipher : str, rotation : int) -> str:
    cipheredMessage = ""
    for character in stringToCipher:
        add cipherCharacter(character, rotation) to end of cipheredMessage
    return cipheredMessage
```

#### Cipher Character
Takes a single character and rotation distance, giving back a ciphered character, applying the Caesar Cipher algorithm detailed above

Returns the newly ciphered character, or the original character if character shouldn't be ciphered

```py
def cipherCharacter(char : str, rot : str) -> str:
    if char is in [A-Z]:
        charBaseVal = ord("A")
    elif char is in [a-z]:
        charBaseVal = ord("a")
    else:
        # Don't cipher this character
        return char
    charOrdVal = ord(char)
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
```

*   Notes
    *   To compute if a character is in [A-Z] or [a-z]...
        *   `ord("A") == 65`
        *   `ord("Z") == 90`
        *   `ord("a") == 97`
        *   `ord("z") == 122`

## Phase 3: Implementation

Implementation went by without a hitch! The design I had seemed to be implemented according to plan. The most notable change from the design was that the `parseCLArgs` function became the `if __name__ == "__main__":` block, as that was the true entrypoint of the function.

I needed to import `sys` for `sys.argv` and `sys.exit`. I also needed to import `typing` so I can have access to the `Optional` type for type hinting. This `typing` module wasn't explicitly listed in the instructions, but I talked with DuckieCorp management (my TA) to be sure it was okay. They told me that was an oversight when DuckieCorp management wrote the instructions, and they intended to give access to the `typing` module as an approved import. Small oversight in the instructions. Pobody's nerfect, I guess!

## Phase 4: Testing & Debugging

## Phase 5: Deployment

## Phase 6: Maintenance
