# X- city
# N - boys
# M - girls
# K - seats in each room of hotel 
# boys can not live with girls
# T denoting no. of test cases   -- 1sr line input


for item in range(int(input())):
    N, M, K = input().split()
    rooms = (int(N)//int(K)) + (int(M)//int(K))
    if (int(N)%int(K)) !=0:
        rooms+=1
    if (int(M)%int(K))!=0:
        rooms +=1
    print(rooms)