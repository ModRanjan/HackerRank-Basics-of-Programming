N = int(input())

listarray = list(map(int, input().split()))
subarray= ''

# odd = 0
# even =0
# for i in range()
for i in range(N):
    if i<N//2:
        subarray += str(listarray[i])[0]
    else:
        subarray += str(listarray[i]%10)

if int(subarray)%11==0:
    print("OUI") 
else:
    print("NON")