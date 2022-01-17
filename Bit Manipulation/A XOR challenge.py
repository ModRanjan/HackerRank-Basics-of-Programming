import math

C = int(input())

p = int(math.log(C, 2))

A = int(pow(2, p)) - 1

B = A ^ C

print(A * B)
