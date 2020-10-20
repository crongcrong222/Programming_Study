 #include <iostream>
 #include <algorithm>
 #include <stack>
 
 using namespace std;
 int arr[1000];
 int main(){
 	ios::sync_with_stdio(0);
    cin.tie(0);
    long long sum=0;
 	int n;
 	stack <int> v;
 	
 	cin>>n;
 	
 	int arr[n+1] = {0};
 	
 	for(int i = 0; i < n ; i++){
 		cin >> arr[i];
 	}
 	
 	
 	for(int i = 0; i < n ; i++){
 		while(!v.empty() && v.top() <= arr[i]){
 			v.pop();
 		}
 		v.push(arr[i]);
 		
 		sum+=v.size() - 1;
 	}

 	cout << sum;
 }
