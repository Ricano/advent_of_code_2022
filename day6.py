from inputs.d6 import d6_list


def resolveday6():
    buffer = []
    buffer2 = []
    start = 0
    end = 4

    start2 = 0
    end2 = 14

    # for i in range(len(d6_list) - 3):
    #     buffer = d6_list[start:end]
    #     start += 1
    #     end += 1
    #     if buffer.count(buffer[0]) == 1 and buffer.count(buffer[1]) == 1 and buffer.count(
    #             buffer[2]) == 1 and buffer.count(
    #         buffer[3]) == 1:
    #         print("BUFFER")
    #         print(i + 4, buffer)

    for j in range(len(d6_list) - 13):
        buffer2 = d6_list[start2:end2]
        start2 += 1
        end2 += 1
        if buffer2.count(buffer2[0]) == 1 and buffer2.count(buffer2[1]) == 1 and buffer2.count(buffer2[2]) == 1 and buffer2.count(
            buffer2[3]) == 1 and buffer2.count(buffer2[4]) == 1 and buffer2.count(buffer2[5]) == 1 and buffer2.count(
            buffer2[6]) == 1 and buffer2.count(buffer2[7]) == 1 and buffer2.count(buffer2[8]) == 1 and buffer2.count(
            buffer2[9]) == 1 and buffer2.count(buffer2[10]) == 1 and buffer2.count(buffer2[11]) == 1 and buffer2.count(
            buffer2[12]) == 1 and buffer2.count(buffer2[13]) == 1:
            print("BUFFER2")
            print(j + 14, buffer2)


"1578"
resolveday6()
