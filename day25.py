with open('inputs/d25.in', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

code = {
    2: "2",
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}


def snafu_to_dec(snafu: str) -> int:
    if len(snafu) == 0:
        return 0
    d = 0
    for i, c in enumerate(snafu[::-1]):
        if c == '-':
            d += -1 * (5 ** i)
        elif c == '=':
            d += -2 * (5 ** i)
        else:
            d += int(c) * (5 ** i)
    return d


def dec_to_snafu(dec: int) -> str:
    i = 0
    snafu = ''
    while True:
        max_range = 2 * (5 ** i)
        for j in range(i):
            max_range += 2 * (5 ** j)
        if max_range >= dec:
            break
        i += 1
    other_center = 0
    for n in range(i, -1, -1):
        other_max = sum([2 * (5 ** j) for j in range(n)])
        for c in code.keys():
            center = c * (5 ** n) + other_center
            if n != 0:
                if center - other_max < dec <= center + other_max:
                    snafu += code[c]
                    other_center = center
                    break
            else:
                if center + other_max == dec:
                    snafu += code[c]
                    break

    return snafu


decs = [snafu_to_dec(x) for x in lines]
snafus = [dec_to_snafu(x) for x in decs]

dec_sum = sum(decs)
print("D25P1:", dec_to_snafu(dec_sum))
