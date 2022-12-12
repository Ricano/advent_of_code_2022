import os

the_list = []
for line in open("inputs/9.in").readlines():
    the_list.append(line.strip())

LEFT = [-1, 0]
RIGHT = [1, 0]
UP = [0, 1]
DOWN = [0, -1]
LENGTH = 50
rows, cols = (LENGTH, LENGTH)
arr = [[" " for i in range(LENGTH)]for i in range(LENGTH)]
def print_array(a):
    print('\n'*100)
    for x in a:
        print(str(x).lstrip("[").rstrip("]").replace(",", ""))


mov = (0, 0)

tx, ty, hx, hy = 25, 25, 25, 25


arr[hx][hy]="H"
#print_array(arr)

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
    for j in range(n):
        px = hx
        py = hy
        hx += mov[0]
        hy += mov[1]
        arr[tx][ty] = "T"
        arr[hx][hy] = "H"
        arr[px][py] = " " if arr[px][py] != "T" else "T"

#        print("STEP:", i, j)

    print_array(arr)
    print(i)
    print(d, n)
    print(hx, hy)

