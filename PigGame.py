import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number must be between 2 and 4")
    else:
        print("Invalid, try again!")

max_score =20
player_scores = [0 for _ in range(players)]

while max(player_scores) <= max_score:
    for player_index in range(players):
        print("\nPlayer ", player_index+1, " turn has started!")
        print("\nYour current score is ", player_scores[player_index], " \n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll (y)? : ")
            if should_roll.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("You rolled a 1")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rolled a ", value)

        player_scores[player_index] += current_score
        print("Your total score is ", player_scores[player_index])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number : ", winning_idx + 1, " You won with a score of ", max_score)


