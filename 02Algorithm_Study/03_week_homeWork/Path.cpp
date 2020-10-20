#include <string>
#include <iostream>
#include <vector>
int myMap[110][110];
int visit[110][110];
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    visit[1][1] = 1;
    for(int i = 0; i <puddles.size(); i++){
        myMap[puddles[i][1]][puddles[i][0]] = 1;
    }

    for(int i = 1; i <=n; i++){
        for(int j = 1; j <=m; j++){
            if(i !=1 || j !=1){
                if(myMap[i][j] == 1){
                    visit[i][j] = 0;
                }
                else{
                    visit [i][j] = (visit[i-1][j] + visit[i][j-1])%1000000007;
                }
            }
        }
    }
    answer = visit[n][m];
    return answer;
}

int main(){
    cout << solution(4,3,{{2,2}});
}