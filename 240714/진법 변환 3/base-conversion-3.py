import sys

first_input = sys.stdin.readline()

decimal = 0
for i in range(len(first_input)):
    decimal += int(first_input[i]) * 8**(len(first_input)-i-1)

result = []

while decimal != 0:
    if decimal % 2 == 0:
        result.append(0)
    else:
        result.append(1)
    decimal = decimal // 2

for i in range(len(result)):
    print(result[len(result)-i-1], end="")