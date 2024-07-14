import sys

n = int(sys.stdin.readline())

A = list(sys.stdin.readline().split())
B = list(sys.stdin.readline().split())
C = list(sys.stdin.readline().split())
D = list(sys.stdin.readline().split())

A_result = 0
for i in range(1, n+1):
    A_result += int(A[i])

B_result = 0
for i in range(1, n+1):
    B_result += int(B[i])

C_result = 0
for i in range(1, n+1):
    C_result += int(C[i])

D_result = 0
for i in range(1, n+1):
    D_result += int(D[i])

result = []
result.append(A_result)
result.append(B_result)
result.append(C_result)
result.append(D_result)

result.sort()

print("A - " + str(A_result))
print("B - " + str(B_result))
print("C - " + str(C_result))
print("D - " + str(D_result))

if result[-1] == A_result:
    print("Class A is winner!")

elif result[-1] == B_result:
    print("Class B is winner!")

elif result[-1] == C_result:
    print("Class C is winner!")

else:
    print("Class D is winner!")