T = int(input())

mxdata = []
for i in range(T):
    N,M= input().split()

N = int(N)

for i in range(1, (N+1)):
    for j in range(1, (N+1)):
        mxdata.append((i+j))

# print(mxdata)    
count = 0
def primeFactor(N):
    count = 0
    if N<=1:
        return count
    i=2
    while i*i<N:
        while N%i == 0:
            # print(i)
            count+=1
            N = N/i
        i+=1
    if N>1:
        count += 1
    return count

total = 0
for i in range(len(mxdata)):
    total+=(primeFactor(mxdata[i]))
    

print(total)