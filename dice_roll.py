import random

print("Use word 'roll' or 'r' only to proceed the game :")

def player_1():
    global player_1_number
    player_1_number = random.randint(1,6)
    return player_1_number
    
def player_2():
    global player_2_number
    player_2_number = random.randint(1,6)
    return player_2_number

score_player_1 = 0
score_player_2 = 0
chances = 1    
while chances <= 5:
    
    # For Player 1
    player_1_turn = input("\nPlayer 1 Turn : ")
    player_1_turn = player_1_turn.lower().strip()
    
    if player_1_turn == "roll" or player_1_turn == "r":
        player_1()
        print("Dice Generated Number for P1 :", player_1_number)
        score_player_1 = score_player_1 + player_1_number
        print("Player 1 Score yet :", score_player_1)
        print("Dice Rolled" + " " + str(chances) + "time(s) for P1")
    else:
        print("Please Enter the word 'roll' or 'y'!!")
        
    # For Player 2
    player_2_turn = input("\nPlayer 2 Turn :")
    player_2_turn = player_2_turn.lower().strip()
    
    if player_2_turn == "roll" or player_2_turn == "r":
        player_2()
        print("Dice Generated Number for P2 :", player_2_number)
        score_player_2 = score_player_2 + player_2_number
        print("Player 2 Score Yet :", score_player_2)
        print("Dice Rolled" + " " + str(chances) + "time(s) for P2")
    else:
        print("Please Enter the word 'roll' or 'y'!!")
    chances = chances + 1
    
print("\nPlayer 1 Score :", str(score_player_1) + "points")
print("Player 2 Score :", str(score_player_2) + "points")

if score_player_1 > score_player_2:
    print("\nPlayer 1 has Won!!")
    
elif score_player_1 < score_player_2:
    print("\nPlayer 2 has Won!!")
    
else:
    print("Game Tied!!")