def resolve_day7():
    stack = []
    sizes = []

    def up():
        sizes.append(stack.pop(-1))
        if stack:
            stack[-1] += sizes[-1]

    for line in open("inputs/7.in").readlines():
        print(stack)

        match line.strip().split():
            case "$", "cd", "..":
                up()
            case "$", "cd", _:
                stack.append(0)
            case "$", _:
                pass
            case "dir", _:
                pass
            case size, _:
                stack[-1] += int(size)

    while stack:
        up()

    print(stack)
    print(sizes)
    print(sum(s for s in sizes if s <= 100000))
    print(min(s for s in sizes if s >= (max(sizes) - 40000000)))


resolve_day7()
