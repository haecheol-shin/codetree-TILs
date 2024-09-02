n, t = map(int, input().split())
r, c, d = input().split()

d_dict = {'U': 1, 'D': 2, 'R': 0, 'L': 3}
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

x = int(c) - 1
y = int(r) - 1

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(t):
    nx = x + dx[d_dict[d]]
    ny = y + dy[d_dict[d]]

    if in_range(nx, ny) is False:
        d_dict[d] = 3 - d_dict[d]

    else:
        x = nx
        y = ny

print(y+1, x+1)