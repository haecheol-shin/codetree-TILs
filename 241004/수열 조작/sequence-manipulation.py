from collections import deque

N = int(input())

numbers = deque()
for i in range(1, N+1):
    numbers.append(i)

while len(numbers) != 1:
    numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[0])