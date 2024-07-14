import sys

n_m = list(map(int, sys.stdin.readline().split()))

n = n_m[0]
m = n_m[1]

result = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    a_b_c = list(map(int, sys.stdin.readline().split()))
    a = a_b_c[0]
    b = a_b_c[1]
    c = a_b_c[2]

    if a == 1:
        result[b-1] = c
    
    elif a == 2:
        for i in range(b-1,c):
            if result[i] == 0:
                result[i] = 1
            else:
                result[i] = 0

    elif a == 3:
        for i in range(b-1,c):
            result[i] = 0
    
    else:
        for i in range(b-1,c):
            result[i] = 1

for i in result:
    print(i, end = " ")