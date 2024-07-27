import sys

sentence = sys.stdin.readline()

stack = []

for i in sentence:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) == 0 or stack[-1] != '(':
            print("No")
        else:
            stack.pop()
        
if len(stack) != 0:
    print("No")
else:
    print("Yes")