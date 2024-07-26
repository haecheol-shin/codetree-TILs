import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == "push":
        result.append(int(command[1]))
    
    elif command[0] == "size":
        print(len(result))
    
    elif command[0] == "pop":
        print(result.pop())

    elif command[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    
    else:
        if len(result) == 0:
            print("empty")
        else:
            print(result[-1])