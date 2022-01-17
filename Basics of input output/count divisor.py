l , r ,k = (input().split())

count =0
for item in range(int(l), int(r)+1):
    if item % int(k) == 0 :
        count+=1
print(count)