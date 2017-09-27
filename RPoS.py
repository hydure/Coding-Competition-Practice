numberOfGames = int(input())
results = [0] * numberOfGames
gameCounter = 0

while gameCounter != numberOfGames:
    numberOfRounds = int(input())
    player1 = 0
    player2 = 0
    roundCounter = 0

    while roundCounter != numberOfRounds:
        result = input()
        if ((result == "P R") or (result == "S P") or (result == "R S")):
            player1 += 1
        if ((result == "R P") or (result == "P S") or (result == "S R")):
            player2 += 1
        roundCounter += 1
    
    if player1 > player2:
        results[gameCounter] = "Player 1"
    elif player2 > player1:
        results[gameCounter] = "Player 2"
    else:
        results[gameCounter] = "TIE"
    gameCounter += 1

for result in results:
    print(result)