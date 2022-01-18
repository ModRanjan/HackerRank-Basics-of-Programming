arr=input().strip()
count=0
 
for i in range(len(arr)):
    flag=0
    if arr[i]=='(':
        for j in range(i,len(arr)+i):
            if arr[j%len(arr)]=='(':
                flag+=1
            else:
                flag-=1
            if flag<0:
                break
        if flag==0:
            count+=1

 
print(count)