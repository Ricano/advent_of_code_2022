from inputs.d1 import d1_list


def resolve_day1():
    number_of_elves = 0
    total_calories = 0
    calories_per_elf = [[]]

    for item in d1_list:
        if item != "":
            calories_per_elf[number_of_elves].append(item)
            total_calories += int(item)
        else:
            number_of_elves += 1
            calories_per_elf.append([])

    total_calories_per_elf = []

    for item in calories_per_elf:
        sum = 0
        for value in item:
            sum += int(value)
        total_calories_per_elf.append(sum)

    max = 0
    for x in total_calories_per_elf:
        if int(x) > max:
            max = int(x)

    total_calories_per_elf.sort(reverse=True)
    top3 = total_calories_per_elf[0]+total_calories_per_elf[1]+total_calories_per_elf[2]
    #
    # print("number_of_elves: ", number_of_elves + 1)
    # print("total_calories:", total_calories)
    # print("calories_per_elf_list:", calories_per_elf)
    # print("len_calories_per_elf_list:", len(calories_per_elf))
    # print("total_calories_per_elf:", total_calories_per_elf)
    # print("len_total_calories_per_elf:", len(total_calories_per_elf))
    # print("MAX TOTAL CALORIES CARRIED BY ONE ELF: ", max)
    # print("TOTAL CALORIES CARRIED BY TOP 3 ELVES: ", top3)
    #
    print("D1P1:", max)
    print("D1P2:", top3)

