from inputs.d5 import d5_list, s1, s2, s3, s4, s5, s6, s7, s8, s9

s = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def resolve_day5():
    for instruction in d5_list:
        _, amount, _, start, _, end = instruction.split(" ")

        amount= int(amount)
        start= int(start)-1
        end= int(end)-1

        start = s[start]
        end = s[end]
        print(amount)

        for i in range(int(amount)):
            end.append(start[-1])
            start.remove(start[-1])
        print(start)
        print(end)
    print("XXX")
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s7)
    print(s8)
    print(s9)
resolve_day5()

"HHVGGVPL"
