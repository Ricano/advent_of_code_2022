from inputs.d7 import d7_list

dict_tree = {"/": []}

current = None
previous = None


def resolve_day7():
    for x in d7_list:
        start = x.split(" ")[0]
        if start == "$":
            # check command
            command = x.split(" ")[1]
            if command == "cd":
                end = x.split(" ")[2]
                if end == "/":
                    current = "/"
                    previous = None
                elif end == "..":
                    current = previous
                else:
                    previous = dict_tree[current]
                    current = previous[end]
            elif command == "ls":
                continue
        elif start == "dir":
            dir = x.split(" ")[1]
            dict_tree[current].append({dir:[]})

        print(dict_tree)


resolve_day7()
