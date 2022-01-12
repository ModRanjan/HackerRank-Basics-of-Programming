#include <iostream>
#include <string>
# using namespace std;

# int main() {
# 	string str;
# 	cin >> str;										// Reading input from STDIN
# 	int count =0;
# 	int length= str.length();
# 	for(int i=0; i<length; i++){
# 		if(str[i]=='z')
# 			count+=1;
# 	}
# 	if(count*2 == (length-count))
# 		cout << "Yes" << endl;		// Writing output to STDOUT
# 	else
# 		cout << "No" << endl;	
# }

n=input()
p=0
q=0
for i in n:
    if i=='z':
        p+=1
    elif i=='o':
        q+=1
if p*2==q:
    print("Yes")
else:
    print("No")