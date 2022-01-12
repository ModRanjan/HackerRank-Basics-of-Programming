n=int(input())
array1=list(map(int,input().split()))
array2=list(map(int,input().split()))
mindata=min(array1)
i=0
count=0
while i<n:
    while array1[i]>mindata:
        array1[i]=array1[i]-array2[i]
        count+=1
    if array1[i]<mindata:
        mindata=array1[i]
        i=0
    elif array1[i]<0:
        count=-1
        break
    else:
        i+=1
print(count)