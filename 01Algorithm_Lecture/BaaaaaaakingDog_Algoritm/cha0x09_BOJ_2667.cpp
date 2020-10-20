#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int myMap[26][26];
int visit[26][26];
int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
vector<int> cntDanji={0};
int n;

void bfs(int sx, int sy, int danji){

    queue <int> q;
    q.push(sx);
    q.push(sy);
    visit[sx][sy] = danji;
    int cnt = 1;
    while(!q.empty()){
        int x = q.front();
        q.pop();
        int y = q.front();
        q.pop();
        for(int dir = 0; dir< 4; dir++){
            int cx = x + dx[dir];
            int cy = y + dy[dir];
            if(cx<0||cy<0||cx>=n||cy>=n){
                continue;
            }
            else{
                if(myMap[cx][cy] == 1 && visit[cx][cy] == 0){
                    q.push(cx);
                    q.push(cy);
                    visit[cx][cy] = danji;
                    cnt ++;
                }
            }
        }

    }
    cntDanji.push_back(cnt);
}


int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);
    string tmp;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> tmp;
        for(int j = 0; j < n ; j++){
            myMap[i][j] = tmp[j] - '0';
        }
    }
    int danji = 0;
    for(int i = 0; i < n ; i ++){
        for(int j = 0; j < n; j++){
            if(myMap[i][j] == 1 && visit[i][j] == 0){
                danji ++;
                
                bfs(i, j, danji);
            }
        }
    }

    sort(cntDanji.begin(),cntDanji.end());
    cout<<danji << '\n';
    for(int i = 1 ; i < cntDanji.size() ;i++){
        cout << cntDanji[i]<<'\n';
    }

}