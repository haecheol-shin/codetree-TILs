n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

matrix = []
for i in range(n):
    matrix.append(input().split())

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n


result = 0
x = 0
y = 0
for i in range(n):
    for j in range(n):
        count = 0
        for nx, ny in zip(dx, dy):
            x = i + nx
            y = j + ny
            if in_range(x, y) and matrix[x][y] == '1':
                count += 1
        if count >= 3:
            result += 1

print(result)