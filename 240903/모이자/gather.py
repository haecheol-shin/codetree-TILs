n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    distance = 0
    for j in range(len(arr)):
        distance += arr[j] * abs(j-i)
    result.append(distance)

result.sort()
print(result[0])