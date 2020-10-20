#include <bits/stdc++.h>

using namespace std;

int dp[10001];
int n,m;

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >>n >>m;

    dp[0] = 1;

    for(int i = 1; i <= n; i++){
        dp[i] = dp[i-1];
        if(i-m>=0){
            dp[i] = (dp[i] + dp[i-m])%1000000007;
        }
    }
    cout << dp[n];
}

