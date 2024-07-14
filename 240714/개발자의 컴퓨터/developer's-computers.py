import sys

N = int(sys.stdin.readline())

result = [0] * 999
for i in range(N):
    s_t_b = list(map(int, sys.stdin.readline().split()))
    s = s_t_b[0]
    t = s_t_b[1]
    b = s_t_b[2]

    for i in range(s-1, t):
        result[i] += b

result.sort()
print(result[-1])