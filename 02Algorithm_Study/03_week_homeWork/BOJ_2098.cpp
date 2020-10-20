#include <bits/stdc++.h>

using namespace std;

int n;
int myMap[17][17];
int dp[16][1<<16];

int tsp(int cur, int visit){
    int result;
    int re = dp[cur][visit];

    if (re != 0){
        return re;
    }
    if(visit ==(1<<n)-1){
        if(myMap[cur][0] != 0){
            return myMap[cur][0];
        }
        else{
            return 1000000000;
        }
    }
    re = 1000000000;

    for (int i = 0; i < n; i ++){
        if((visit&(1<<i))|| (myMap[cur][i] == 0)){
            continue;
        }
        result = tsp(i,(visit|1<<i)) + myMap[cur][i];
        if(result < re){
            re = result;
        }
    }
    dp[cur][visit] = re;
    return re;
}

int main (){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i  = 0; i < n ; i++){
        for(int j = 0; j < n; j++){
            int tmp ;
            cin >>tmp;
            myMap[i][j] = tmp;
        }
    }

    cout << tsp(0,1);
}