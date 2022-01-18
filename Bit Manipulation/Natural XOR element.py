"""1- Find the remainder of n by moduling it with 4. 

2- If rem = 0, then xor will be same as n. 

3- If rem = 1, then xor will be 1. 

4- If rem = 2, then xor will be n+1. 

5- If rem = 3 ,then xor will be 0

"""

N=int(input())

for i in range(N):
    T=int(input())
    r=T%4
    if r==3:
        print(0)
    elif r==1:
        print('1','1')
    elif r==2:
        print('2',T,'1')  

    else:
        print('1',T)
