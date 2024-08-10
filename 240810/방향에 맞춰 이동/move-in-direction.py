x = 0
y = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N = int(input())

for i in range(N):
    direction, distance = input().split()

    if direction == 'N':
        x += dx[1] * int(distance)
        y += dy[1] * int(distance)

    elif direction == 'S':
        x += dx[3] * int(distance)
        y += dy[3] * int(distance)
    
    elif direction == 'E':
        x += dx[0] * int(distance)
        y += dy[0] * int(distance)

    else:
        x += dx[2] * int(distance)
        y += dy[2] * int(distance)

print(x, y)