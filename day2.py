from inputs.d2 import d2_list


def resolve_day2():
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
    CODE2 = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "loose",
        "Y": "draw",
        "Z": "win",
    }
    score = 0
    score2 = 0

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

    def get_my_play(opp, n):
        if opp == "rock":
            if n == "draw":
                return "rock"
            elif n == "win":
                return "paper"
            else:
                return "scissors"
        elif opp == "scissors":
            if n == "draw":
                return "scissors"
            elif n == "win":
                return "rock"
            else:
                return "paper"
        else:
            if n == "draw":
                return "paper"
            elif n == "win":
                return "scissors"
            else:
                return "rock"

    for item in list:
        opponent = CODE[item[0]]
        me = CODE[item[1]]
        score += SCORES[me] + game_result(me, opponent)

    for item in list:
        opponent = CODE2[item[0]]
        need = CODE2[item[1]]

        me = get_my_play(opponent, need)

        score2 += SCORES[me] + game_result(me, opponent)

    print("Day 2 - ", "D2P1:", score, " D2P2:", score2)
