with open('inputs/d21.in', 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def monkey_eval(monkey_name, monkey_dict):
    monkey_yell = monkey_dict[monkey_name]
    if isinstance(monkey_yell, int):
        return monkey_yell
    else:
        if monkey_yell[1] == '/':
            return monkey_eval(monkey_yell[0], monkey_dict) / monkey_eval(monkey_yell[2], monkey_dict)
        elif monkey_yell[1] == '+':
            return monkey_eval(monkey_yell[0], monkey_dict) + monkey_eval(monkey_yell[2], monkey_dict)
        elif monkey_yell[1] == '-':
            return monkey_eval(monkey_yell[0], monkey_dict) - monkey_eval(monkey_yell[2], monkey_dict)
        elif monkey_yell[1] == '*':
            return monkey_eval(monkey_yell[0], monkey_dict) * monkey_eval(monkey_yell[2], monkey_dict)
        elif monkey_yell[1] == '=':
            return monkey_eval(monkey_yell[0], monkey_dict) == monkey_eval(monkey_yell[2], monkey_dict)


monkey_dict = {}

for line in lines:
    monkey_name, monkey_yell = [x.strip() for x in line.split(':')]
    monkey_yell = [x for x in monkey_yell.split()]
    if len(monkey_yell) == 1:
        monkey_yell = int(monkey_yell[0])
    monkey_dict[monkey_name] = monkey_yell



print("D21P1:", int(monkey_eval('root', monkey_dict)))


