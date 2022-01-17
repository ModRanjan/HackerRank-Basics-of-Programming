for _ in range(int(input())):

    n = int(input())

    arr = set(map(int, input().split()))

    xor = 0



for i in arr:

    xor ^= i



for i in arr:

    temp = i ^ xor

    if temp not in arr:

        print(-1)

        break

    else:

        print(xor)