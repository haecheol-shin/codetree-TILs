def boundary(x, y, n):
    return 0 <= x+2 and x+2 < n and 0 <= y+2 and y+2 < n


def counting(x, y, result):
    count = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if matrix[i][j] == '1':
                count += 1
    result.append(count)

n = int(input())

matrix = []
for i in range(n):
    matrix.append(input().split(' '))

x = 0
y = 0
result = []

for i in range(n):
    for j in range(n):
        if boundary(i, j, n):
            counting(i, j, result)

print(max(result))