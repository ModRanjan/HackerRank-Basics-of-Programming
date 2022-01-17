import math
num = int(input())
arr = list(map(int, input().split()))
ans =1
for item in range(num):
    ans = (ans * arr[item])% (pow(10,9)+7)
    

print(ans)