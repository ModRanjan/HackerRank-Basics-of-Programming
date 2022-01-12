testCases = int(input())
for i in range(testCases):
	N,M = input().split()    # N = lunch boxes
	N= int(N)               # M = schools
	A = list(map(int, input().split()))  # A[i]= lunchboxes
	A.sort()
	A = A[::-1]
	temp = A.pop()
	count = 0
	while N>=temp and len(A)>0:
		count +=1
		N-=temp
		temp=A.pop()
	if len(A)==0 and N>temp:
		print(count+1)
	else:
		print(count)