testCases = int(input())

for i in range(testCases):
    n = int(input())
    ldata = list(map(int, input().split()))

    l2 = []
    l3 = []

    for j in range(len(ldata)):
        if ldata[j]&1==0:
            l2.append(ldata[j])
        else:
            l3.append(ldata[j])

    if len(l2)<len(l3):
        for j in range(len(ldata)):
            if ldata[j]&1==0:
                ldata[j]=0
    else:
        for j in range(len(ldata)):
            if ldata[j]&1!=0:
                ldata[j]=0

    print(ldata.count(0))
    