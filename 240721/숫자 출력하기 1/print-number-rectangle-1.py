import sys

n, m = sys.stdin.readline().split()

number = 1
for i in range(int(n)):
    for j in range(int(m)):
        print(number, end=" ")
        number += 1
    print()