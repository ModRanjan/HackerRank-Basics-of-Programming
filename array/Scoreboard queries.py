testCase = int(input())
while testCase:
    testCase -= 1
    N, Q = map(int,input().split())
    sdata = list(map(int,input().split()))
    pos = []
    while Q:
        l,r = map(int,input().split())
        sdata[l-1] = r
        x = set(sdata)
        Q = Q-1
        print(len(x)+1)