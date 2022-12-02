from inputs.d2 import d2_list

list = d2_list

SCORES = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}
CODE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
score = 0

def game_result(me, opponent):
    if me == "rock":
        if opponent == "rock":
            return 3
        elif opponent == "scissors":
            return 6
        else:
            return 0
    elif me == "paper":
        if opponent == "rock":
            return 6
        if opponent == "scissors":
            return 0
        else:
            return 3
    else:
        if opponent == "rock":
            return 0
        if opponent == "scissors":
            return 3
        else:
            return 6


for item in list:
    opponent = CODE[item[0]]
    me = CODE[item[1]]
    score += SCORES[me] + game_result(me, opponent)

    print(opponent, me, score)

print("FINAL SCORE:", score)
