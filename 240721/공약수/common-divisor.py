import math, sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

if n==2:
    gcd = math.gcd(number[0], number[1])

elif n==3:
    gcd = math.gcd(number[0], number[1], number[2])

result = []
i = gcd
while i != 1:
    if gcd % i == 0:
        result.append(i)
    i -=1
result.append(1)
result.sort()
for i in result:
    print(i)