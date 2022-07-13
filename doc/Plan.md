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

## Phase 3: Implementation

## Phase 4: Testing & Debugging

## Phase 5: Deployment

## Phase 6: Maintenance
