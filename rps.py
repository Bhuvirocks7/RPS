import sys
import random
from enum import Enum
global game_count
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
while True:
    print("")
    playerchoice = input("Enter your choice ... \n1 for rock, \n2 for paper, or \n3 for scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1, 2 or 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")
    print("you chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    def decide_winner(player, computer):
        
        if player == computer:
            return "🤝It's a tie!"
        elif player == 1 and computer == 3:
            return "🎉You win"
        elif player == 2 and computer == 1:
            return "🎉You win"
        elif player == 3 and computer == 2:
            return "🎉You win"
        else:
            return "🐍Python wins"
    game_result = decide_winner(player, computer)    
    print(game_result)

    game_count = 0
    game_count += 1
    print("\nGames played: " + str(game_count))

    playagain = input("\nPlay again? \n Y for Yes or \nQ to Quit ")

    if playagain.lower() != "y":
        print("\n🎉🎉🎉🎉")
        break
    else:
        print("Let's play again!")
        continue