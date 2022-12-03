from inputs.d3 import d3_list, priorities


def resolve_day3():


    new_list = []

    for item in d3_list:
        l = len(item)
        new = []
        new.append(item[:int(l/2)])
        new.append(item[int(l/2):])

        new_list.append(new)

    repeated_list=[]
    for bag in new_list:
        comp1=bag[0]
        comp2=bag[1]
        for item in comp1:
            if item in comp2:
                repeated_list.append(item)
                break

    total = 0
    for letter in priorities:
        total += priorities[letter]


    print(ord('a'))
    print(ord('b'))
    print(ord('Z'))
    print(ord('A'))
    print(len(repeated_list))
    print(repeated_list)
    print(d3_list[0])
    print(new_list[0][0])
    print(new_list[0][1])
    print("TOTAL: ", total)
