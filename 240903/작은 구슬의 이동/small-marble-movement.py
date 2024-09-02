n, t = map(int, input().split())
r, c, d = input().split()

d_dict = {'R': 1, 'L': 2, 'U': 0, 'D': 3}
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

x = int(r) - 1
y = int(c) - 1

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
    

print(x+1, y+1)