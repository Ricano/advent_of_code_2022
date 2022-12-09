from inputs.d8 import d8_list

grid = [[int(tree) for tree in line.strip()] for line in d8_list]

edges = 4 * len(grid) - 4
inner = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        # check north
        if all(grid[k][j] < grid[i][j] for k in range(0, i)):
            inner += 1
            continue
        # check east
        if all(grid[i][k] < grid[i][j] for k in range(j + 1, len(grid[i]))):
            inner += 1
            continue
        # check south
        if all(grid[k][j] < grid[i][j] for k in range(i + 1, len(grid))):
            inner += 1
            continue
        # check west
        if all(grid[i][k] < grid[i][j] for k in range(0, j)):
            inner += 1
            continue



# ## Part Two


def get_scenic_score(grid, i, j):
    # get north
    north_score = 0
    for k in range(i - 1, -1, -1):
        north_score += 1
        if grid[k][j] >= grid[i][j]:
            break

    # get east
    east_score = 0
    for k in range(j + 1, len(grid[i])):
        east_score += 1
        if grid[i][k] >= grid[i][j]:
            break

    # get south
    south_score = 0
    for k in range(i + 1, len(grid)):
        south_score += 1
        if grid[k][j] >= grid[i][j]:
            break
    # get west
    west_score = 0
    for k in range(j - 1, -1, -1):
        west_score += 1
        if grid[i][k] >= grid[i][j]:
            break

    return north_score * east_score * south_score * west_score


max_score = max(get_scenic_score(grid, i, j) for i in range(len(grid)) for j in range(len(grid[0])))
print("d8p1", edges + inner)

print("d8p2", max_score)
