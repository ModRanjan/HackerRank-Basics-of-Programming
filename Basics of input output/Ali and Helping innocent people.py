arr= input()
result =0
status =0
subStr={"A","E","I","O","U","Y"}

if arr[2] in subStr :
    print("invalid")
elif (int(arr[0])+int(arr[1])%2)==0 or (int(arr[3])+int(arr[4])%2)==0 or (int(arr[4])+int(arr[5])%2)==0 or (int(arr[7])+int(arr[8])%2)==0:
    print("valid")
else:
    print("invalid")