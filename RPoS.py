import fileinput
import string

gameOn = 0
previousGame = 0

for line in fileinput.input():
    
    # Get that pesky newline char off and check if first digit
    if line.strip().isdigit() and gameOn == 0:
        gameOn += 1
        continue

    # A new game has begun!
    if line.strip().isdigit() and gameOn == 1:
        
        numberOfRounds = int(line.strip())

        # Start a new game
        player1 = 0
        player2 = 0
        continue
    
    # Get each player's actions
    line = line.strip().split()
    numberOfRounds -= 1
    
    # If Player 2 wins the round
    if (line[0] == 'R' and line[1] == 'P') or \
       (line[0] == 'P' and line[1] == 'S') or \
       (line[0] == 'S' and line[1] == 'R'):
        player2 += 1
    
    # If tie
    elif (line[0] == line[1]):
        continue

    # If Player 1 wins the round
    else:
        player1 += 1
    
    if numberOfRounds == 0:
        if player1 > player2:
            print("Player 1")
        elif player2 > player1:
            print("Player 2")
        else:
            print("TIE")

'''
Rock, Paper, Scissors is a two player game, where each player simultaneously chooses one of the three items
after counting to three. The game typically lasts a pre-determined number of rounds. The player who wins the
most rounds wins the game. Given the number of rounds the players will compete, it is your job to determine
which player wins after those rounds have been played.
The rules for what item wins are as follows:
• Rock always beats Scissors (Rock crushes Scissors)
• Scissors always beat Paper (Scissors cut Paper)
• Paper always beats Rock (Paper covers Rock)

Input
The first value in the input file will be an integer t (0 < t < 1000) representing the number of test cases in the
input file. Following this, on a case by case basis, will be an integer n (0 < n < 100) specifying the number of
rounds of Rock, Paper, Scissors played. Next will be n lines, each with either a capital R, P, or S, followed by
a space, followed by a capital R, P, or S, followed by a newline. The first letter is Player 1's choice; the
second letter is Player 2's choice.

Output
For each test case, report the name of the player (`Player 1' or `Player 2') that wins the game, followed
by a newline. If the game ends up in a tie, print `TIE'.

Sample Input
3
2
R P
S R
3
P P
R S
S R
1
P R

Sample Output
Player 2
TIE
Player 1
'''
