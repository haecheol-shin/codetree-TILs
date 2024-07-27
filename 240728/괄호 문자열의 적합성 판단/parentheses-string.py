import sys

def func(sentence):
    stack = []
    for i in sentence:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or stack[-1] != '(':
                return print("No")
            else:
                stack.pop()
            
    if len(stack) != 0:
        return print("No")
    else:
        return print("Yes")

def __main__:
    sentence = sys.stdin.readline()
    func(sentence)