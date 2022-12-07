from inputs.d5 import d5_list, s1, s2, s3, s4, s5, s6, s7, s8, s9



def resolve_day5():
    s = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    for instruction in d5_list:
        _, amount, _, start, _, end = instruction.split(" ")

        amount = int(amount)
        start = int(start) - 1
        end = int(end) - 1

        start = s[start]
        end = s[end]
        # print(amount)
        # print(start)
        # print(end)
        # for i in range(int(amount)):
        #     end.append(start.pop(-1))
        transfer = start[-amount:]
        [end.append(x) for x in transfer]
        for i in range(int(amount)):
            start.pop(-1)
        print(start)
        # print(end)
        # print("XXX")
        # print(s1)
        # print(s2)
        # print(s3)
        # print(s4)
        # print(s5)
        # print(s7)
        # print(s8)
        # print(s9)

    print("D5P1", "".join(([str(x[-1][0]) for x in s])))

resolve_day5()
"HHVGGVPL"
"VCTFTQCG"
