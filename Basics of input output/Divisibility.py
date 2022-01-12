# #include <iostream>

# using namespace std;

# int main() {
# 	long long int n;
# 	cin >> n;
# 	// long long int arr[n];
# 	// for (int i = 0; i < n; ++i)
#     // 	scanf("%ld", &arr[i]);

# 	long int m;
# 	for(long i =1; i<=n;i++){
# 		scanf("%ld",&m);
# 	}
# 	if(m%10==0)
# 		printf("Yes");
# 	else
# 		printf("No");
# 			// Writing output to STDOUT
# }

n=int(input())
ldata=list(map(int,input().split()))
value=''
for i in range(n):
    value+=str(ldata[i]%10)
if int(value)%10==0:
    print("Yes")
else:
    print("No")