 #include <bits/stdc++.h>
 #define Max_day 16
 
 
 
 int T[Max_day];
 int P[Max_day];
 int DP[Max_day];
 using namespace std;
 
 int max(int a, int b){
 	return a>b ? a : b;
}



 
 int main(void){
 	ios::sync_with_stdio(0);
 	cin.tie(0);
 	cout.tie(0);
 		
 	int n;
 	cin >>n;

 	for(int i = 1; i <= n; i ++){
 		
 		cin >> T[i] >> P[i];

 	}
 	// i일째 받을 수 있는 최대 금액 DP[i] 
	// 1. 일을 안하고넘어감 DP[i] == D[i+1] 
	// 2. 일을 하고 넘어감 DP[i] == P[i] + DP[i + T[i]]
	// 1과 2중 큰 값을 DP[i] 정의함
	 
 	for(int i = n; i >=1 ; i--){
 		if(i + T[i] > n + 1){
 			DP[i] = DP[i+1];
 		}
 		else{
 			DP[i] = max(DP[i+1], (P[i]+DP[i+T[i]]));
 		}
 	}
 	cout <<DP[1];
 	return 0;
 }
