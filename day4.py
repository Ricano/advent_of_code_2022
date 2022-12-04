from inputs.d4 import d4_list


def resolve_day4():
    contains = 0
    overlaps = 0

    for pair in d4_list:
        first, second = pair.split(",")

        p1_start, p1_end = first.split("-")
        p2_start, p2_end = second.split("-")

        p1_digits = [x for x in range(int(p1_start), int(p1_end) + 1)]
        p2_digits = [x for x in range(int(p2_start), int(p2_end) + 1)]

        if p1_digits == p2_digits or p1_digits[0] <= p2_digits[0] and p1_digits[-1] >= p2_digits[-1] or p2_digits[0] <= \
                p1_digits[0] and p2_digits[-1] >= p1_digits[-1]:
            contains += 1

        if any(item in p2_digits for item in p1_digits) or any(item in p1_digits for item in p2_digits):
            overlaps += 1

    print("Day 4 - ", "CONTAINS:", contains, " OVERLAPS:", overlaps)
