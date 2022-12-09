the_list = []
for line in open("inputs/9.in").readlines():
    the_list.append(line.strip())
print(the_list)

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)

rows, cols = (1000, 1000)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[499][499]



t_pos = (499,499)
h_pos = (499,499)

for i, line in enumerate(the_list):
    d, n = line.split()
    n = int(n)

    if d == "L":
        mov = LEFT
    if d == "R":
        mov = RIGHT
    if d == "U":
        mov = UP
    if d == "D":
        mov = DOWN
    for i in range(n):
        h_pos += mov
        if abs(t_pos[0] - h_pos[0]) > 1:
            # move tail
            pass

