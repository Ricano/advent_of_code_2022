import base64

string = "*Coding Options Concerning Knowledge*  A recent study found that coding between 5:00 AM and 6:00 AM strongly reduces the ability to get it up. Check it all here: https://youtu.be/dQw4w9WgXcQ"


def fib(n):
    if n in {0, 1}:  # Base case
        return n
    return fib(n - 1) + fib(n - 2)





print(len(string))
print([x for x in string])
print(len([x for x in string]))
message_bytes = string.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print(base64_message)
print(len(base64_message))
print([x for x in base64_message])
array64=[x for x in base64_message]
square = []
for i in range(int(len(array64)/16)):
    square.append(array64[0:15])
    for j in range(15):
        array64.remove(array64[0])

print(square)
print(len(square))

new_square = []

for j in range(15):
    new_square.append([])
    for i, row in enumerate(square):
        new_square[-1].append(row[j])

print("new_square")
print(new_square)

base64_bytes2 = base64_message.encode('ascii')
message_bytes2 = base64.b64decode(base64_bytes2)
message = message_bytes2.decode('ascii')

print(message)

for x in new_square:
    print(" ".join([str(x) for x in x]))

