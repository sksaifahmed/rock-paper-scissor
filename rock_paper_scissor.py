import random
import time
import sys

choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissor"
}

nested_dictionary = {
    "Rock": {"Rock": "It's a Draw!!!", "Paper": "Player 2 Wins!!!", "Scissor": "Player 1 Wins!!!"},
    "Paper": {"Rock": "Player 1 Wins!!!", "Paper": "It's a Draw!!!", "Scissor": "Player 2 Wins!!!"},
    "Scissor": {"Rock": "Player 2 Wins!!!", "Paper": "Player 1 Wins!!!", "Scissor": "It's a Draw!!!"}
}

score_1 = 0
score_2 = 0

while(True):
    print('''
        1. Rock
        2. Paper
        3. Scissor
        ''')
    choice = int(input("Enter your Choice: "))
    if choice not in [1, 2, 3]:
        print("Enter a Valid Option!!!")
        sys.exit(0)

    player_1 = choices[choice]
    player_2 = random.choice(["Rock", "Paper", "Scissor"])

    print("Rock!")
    time.sleep(0.7)

    print("Paper!")
    time.sleep(0.7)

    print("Scissor!\n")
    time.sleep(0.7)

    print(player_1, "-", player_2)
    print()
    print(nested_dictionary[player_1][player_2])
    print()

    if nested_dictionary[player_1][player_2] == 'Player 1 Wins!!!':
        score_1 += 1
    elif nested_dictionary[player_1][player_2] == 'Player 2 Wins!!!':
        score_2 += 1

    print(score_1, "-", score_2)
    print()
