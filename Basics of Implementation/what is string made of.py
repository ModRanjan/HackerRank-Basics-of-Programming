dic = [6,2,5,5,4,5,6,3,7,6]
s = str(input())
ct = 0

for i in s:
    ct+=dic[int(i)]

print(ct)