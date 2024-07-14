import sys

n = int(sys.stdin.readline())

second = list(map(int, sys.stdin.readline().split()))

second.sort()

for i in second:
    print(i, end = " ")