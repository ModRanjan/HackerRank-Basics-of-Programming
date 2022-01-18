N, M = (input().split())

ldata = []
count = 0
sumdata = 0
for item in range(int(N)):
    ldata=list(map(int, input().split()))
    print(ldata)
    for i in range(len(ldata)):
        if int(ldata[item]) & 1 ==0:
            count += 1
    
    for i in range(len(ldata)):
        sumdata = sumdata + int(ldata[i])
        if sumdata & 1 == 0:
                count +=1
print(count)