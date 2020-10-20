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
 	// i��° ���� �� �ִ� �ִ� �ݾ� DP[i] 
	// 1. ���� ���ϰ�Ѿ DP[i] == D[i+1] 
	// 2. ���� �ϰ� �Ѿ DP[i] == P[i] + DP[i + T[i]]
	// 1�� 2�� ū ���� DP[i] ������
	 
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
