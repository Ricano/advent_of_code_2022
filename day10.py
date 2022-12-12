from inputs.d10 import d10_list

x = 1
signal = []

for line in d10_list:
    instruction, value = (line.rstrip().split(" ") + [""])[:2]
    if instruction == "noop":
        signal.append(x)
    elif instruction == "addx":
        #        signal.extend([x, x])
        signal.append(x)
        signal.append(x)
        x += int(value)

print(sum(cycle * signal[cycle - 1] for cycle in range(20, len(signal), 40)))

WIDTH = 40
HEIGHT = 6
for line in range(HEIGHT):
    pixel = ""
    for col in range(WIDTH):
        cycle = col + (line * WIDTH)
        pixel += "XXXX" if abs(col - signal[cycle]) <= 1 else "    "
    print(pixel)
