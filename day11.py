# import operator
#
# ops = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,  # use operator.div for Python 2
#     '%': operator.mod,
#     '^': operator.xor,
# }
#
#
# class Monkey():
#     def __init__(self, pk, items, op, test, throw_if_true, throw_if_false):
#         self.pk = pk
#         self.items = items
#         self.op = op
#         self.test = test
#         self.throw_if_true = throw_if_true
#         self.throw_if_false = throw_if_false
#         self.inspected = 0
#         self.worry = 0
#
#
#
#
#
#
# with open("inputs/d11.in") as f:
#     data = [x for x in f.read().strip().split("\n\n")]
#
#     monkeys = []
#
#     for m in data:
#         x = m.split("\n")
#         pk = x[0].split()[1][0]
#         items = [int(z.strip()) for z in x[1].split(":")[1].split(",")]
#         op = x[2].split(":")[1].split("=")[1].split()[1:]
#         test = int(x[3].strip().split(":")[1].split()[2])
#         t_if_true = int(x[4].split()[-1])
#         t_if_false = int(x[5].split()[-1])
#         monkeys.append(
#             Monkey(pk=pk, items=items, op=op, test=test, throw_if_true=t_if_true, throw_if_false=t_if_false))
#
#     for i in range(20):
#         for monkey in monkeys:
#             for item in monkey.__dict__["items"]:
#                 old = item
#                 operation, amount = monkey.__dict__["op"]
#                 if amount == "old":
#                     amount = old
#
#                 new = ops[operation](int(old), int(amount))
#                 new = new / 3
#                 if new % int(test) == 0:
#                     monkeys[monkey.throw_if_true].items.append(int(new))
#                     monkeys[int(monkey.pk)].items.pop(0)
#
#
#                 else:
#                     monkeys[monkey.throw_if_false].items.append(int(new))
#                     monkeys[int(monkey.pk)].items.pop(0)
#
#
#                 monkey.inspected+=1
#
#         l = [x.inspected for x in monkeys]
#         print(l)
#
# #    print(len(monkeys))


f = open('inputs/d11.in', 'r')
content = f.read()
lines = content.split("\n")
num_monkeys = int((len(lines) - 3) / 6)
all_items = []
steps = []
inspects = []
for i in range(num_monkeys):
    inspects.append(0)

for i in range(num_monkeys):
    items = lines[1 + (7 * i)][16:].split(",")
    for j in range(len(items)):
        items[j] = items[j].strip()
    all_items.append(items)
    steps.append(lines[(2 + i*7):(6 + i * 7)])


class Monkeys:
    # Each monkey is represented by a list within the 2-D List
    items = []
    def __init__(self, all_items):
        self.items = all_items
    def print_monkeys(self):
        print(self.items)

m = Monkeys(all_items)

for l in range(20):
    for i in range(len(steps)):
        change = str(steps[i][0][21:len(steps[i][0])])
        op, num = change.split(" ")[0], change.split(" ")[1]
        div = str(steps[i][1]).split(" ")[3]
        t_monkey = str(steps[i][2]).split(" ")[5]
        f_monkey = str(steps[i][3]).split(" ")[5]
        # For each item the monkey has
        for j in range(len(m.items[i])):
            inspects[i] = inspects[i] + 1
            if op == '*':
                if num == 'old':
                    m.items[i][j] = int(m.items[i][j]) * int(m.items[i][j])
                else:
                    m.items[i][j] = int(m.items[i][j]) * int(num)
            else:
                m.items[i][j] = int(m.items[i][j]) + int(num)
            m.items[i][j] = m.items[i][j] // 3
            if m.items[i][j] % int(div) == 0:
                m.items[int(t_monkey)].append(m.items[i][j])
            else:
                m.items[int(f_monkey)].append(m.items[i][j])
        m.items[i].clear()
m.print_monkeys()

one = max(inspects)
inspects.remove(one)
two = max(inspects)
print(one * two)