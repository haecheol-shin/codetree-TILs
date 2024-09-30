from collections import deque

N = int(input())

deque1 = deque()
for i in range(N):
    command = input().split()

    if command[0] == "push_front":
        deque1.appendleft(command[1])

    elif command[0] == "push_back":
        deque1.append(command[1])
    
    elif command[0] == "pop_front":
        print(deque1.popleft())
    
    elif command[0] == "pop_back":
        print(deque1.pop())
    
    elif command[0] == "size":
        print(len(deque1))
    
    elif command[0] == "empty":
        if len(deque1) == 0:
            print(1)
        
        else:
            print(0)

    elif command[0] == "front":
        print(deque1[0])
    
    elif command[0] == "back":
        print(deque1[-1])
    
    else:
        pass