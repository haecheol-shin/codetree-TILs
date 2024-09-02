n, t = map(int, input().split())
r, c, d = input().split()

d_dict = {'U': 1, 'D': 2, 'R': 0, 'L': 3}
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

x = int(r) - 1
y = int(c) - 1

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(t):
    if in_range(x, y) is False:
        d_dict[d] = 3 - d_dict[d]
    
    else:
        nx = x + dx[d_dict[d]]
        ny = y + dy[d_dict[d]]

        x = nx
        y = ny

print(x+2, y+2)