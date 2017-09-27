import fileinput

for word in fileinput.input():

    # Check how many accepted sentences there are
    acceptedSentences = 0

    # Look through word in reverse order
    for char in word[::-1].strip():

        # Check if Rule 1 is followed
        if char in ['p','q','r','s','t','u','v','x','y','z']:
            acceptedSentences += 1

        # Check if Rule 3 is followed
        elif char in ['C', 'D', 'E', 'I'] and acceptedSentences >= 2:
            acceptedSentences -= 1

        # Check if Rule 2 is followed 
        elif char == 'N' and acceptedSentences >= 1:
            pass

        else:
            acceptedSentences = 0
            break
    
    if (acceptedSentences == 1):
        print("YES")
    else:
        print("NO")
'''
Here are the rules:

0. The only characters in the language are the characters ‘p’ through ‘z’ and ‘N’, ‘C’, ‘D’, ‘E’, and ‘I’.
1. Every character from ‘p’ through ‘z’ is a correct sentence.
2. If s is a correct sentence, then so is Ns.
3. If s and t are correct sentences, then so are Cst, Dst, Est and Ist.
4. Rules 0. to 3. are the only rules to determine the syntactical correctness of a sentence.
You are asked to write a program that checks if sentences satisfy the syntax rules given in Rule 0.
- Rule 4.

Input
The input consists of a number of sentences consisting only of characters ‘p’ through ‘z’ and ‘N’, ‘C’, ‘D’,
‘E’, and ‘I’. Each sentence is ended by a new-line character. The collection of sentences is terminated by
the end-of-file character. If necessary, you may assume that each sentence has at most 256 characters
and at least 1 character.

Output
The output consists of the answers ‘YES’ for each well-formed sentence and ‘NO’ for each not-wellformed
sentence. The answers are given in the same order as the sentences. Each answer is followed
by a new-line character, and the list of answers is followed by an end-of-file character.

Sample Input
Cp
Isz
NIsz
Cqpq

Sample Output
NO
YES
YES
NO
'''