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
    for letter in repeated_list:

        total += priorities[letter]

    group3 = []
    for i in range(int(len(d3_list)/3)):
        h = d3_list[0:3]
        d3_list.remove(d3_list[0])
        d3_list.remove(d3_list[0])
        d3_list.remove(d3_list[0])
        group3.append(h)

    badges_list = []
    for group in group3:
        elf1 = group[0]
        elf2 = group[1]
        elf3 = group[2]
        for item in elf1:
            if item in elf2 and item in elf3:
                badges_list.append(item)
                break

    badges_total = 0
    for letter in badges_list:
        badges_total += priorities[letter]

    # print("len GRoup3: ", len(group3))
    # print("GRoup3: ", group3)
    # print("LEN item list: ", len(badges_list))
    # print("ITEM LIST: ", badges_list)

    print("D3P1: ", total)
    print("D3P2: ", badges_total)
