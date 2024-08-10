dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = 0
y = 0

command = input()

for i in command:
    
    if i == 'R':
        dir += 1

    elif i == 'L':
        dir -= 1
    
    else:
        x += dx[dir]
        y += dy[dir]

    if dir < 0:
        dir = dir + 4
    
    dir = dir % 4

print(x, y)