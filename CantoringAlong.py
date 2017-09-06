import sys
import string
import math

# Take in the source file name
sourceFile = sys.argv[1]
textFile = open(sourceFile)

def replaceDashes(lengthOfString, string):
    
    # Recursively call until base case is reached
    if lengthOfString > 3:
        replaceDashes(lengthOfString/3, string)
    
    # Since strings are immutable in python, had to use a list
    for i in range(int(lengthOfString/3), len(string), int(lengthOfString)):
        for j in range(0, int(lengthOfString/3), 1):
            string[i+j] = " "
    
    # Base Case
    if lengthOfString == len(string):
        printString(string)

def printString(string):
    # Print out list like a string
    for element in string:
        print(element, end = "")
    print()

# Get each order of approximation for a string of dashes with length 3rd order
for line in textFile:

    # Calculate the number of dashes per order of approximation
    numberOfDashes = pow(3, int(line.strip()))
    string = ['-'] * numberOfDashes

    # Recursively call the replacement of dashes
    replaceDashes(numberOfDashes, string)