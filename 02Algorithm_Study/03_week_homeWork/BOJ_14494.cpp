#include <bits/stdc++.h>

int mm = 1e9+7;
long long DP[1001][1001];


using namespace std;



int main(){
	int n,m;
	
	cin >>n >>m;
	DP[1][1] = 1;
	for(int i = 1; i <=n; i++){
		for(int j = 1; j <=m; j++){
			if(i !=1 || j !=1){
				DP[i][j] = (DP[i][j-1]%mm + DP[i-1][j]%mm + DP[i-1][j-1]%mm)%mm;
			}
		}
	}
	cout << DP[n][m];
}
