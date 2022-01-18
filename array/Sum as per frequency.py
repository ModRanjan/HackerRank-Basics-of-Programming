N = int(input())
ldata = list(map(int, input().split()))
ldata = set(ldata)

sum_ = [0]*len(ldata)

for item in ldata:
    count = ldata.count(item)
    sum_[count] += item * count

Q = int(input())

for q in range(0, Q):
    l, r = map(int, input().split())
    print(sum(sum_[l:r+1]))