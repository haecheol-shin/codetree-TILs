import sys

n, m = map(int, sys.stdin.readline().split())

listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

listA.sort()
listB.sort()

result = []
while len(listA) != 0 and len(listB) != 0:
    if listA[-1] > listB[-1]:
        result.append(listA.pop())
    else:
        result.append(listB.pop())

while len(listA) != 0:
    result.append(listA.pop())

while len(listB) != 0:
    result.append(listB.pop())

for i in range(len(result)):
    print(result.pop(), end=" ")