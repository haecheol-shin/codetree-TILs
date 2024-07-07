import sys

binary = sys.stdin.readline()

decimal = 0
for i in range(len(binary)):
    decimal += int(binary[i]) * 2**(len(binary)-i-1)

decimal *= 17

result = []
while decimal != 0:
    if decimal % 2 == 0:
        result.append(0)
    else:
        result.append(1)
    decimal = decimal//2
    
for i in range(len(result)):
    print(result.pop(), end="")