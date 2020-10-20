#include <bits/stdc++.h>

using namespace std;

char myMap[1001][1001];
int visit[1001][1001];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
int test_case,n,m;
struct fire {
    int y, x, f;
};
queue <fire> q;



void bfs(){
    while(!q.empty()){
        int y = q.front().y;
        int x = q.front().x;
        int f = q.front().f;
        q.pop();
        for(int dir = 0; dir < 4; dir++){
            int cy = y + dy[dir];
            int cx = x + dx[dir];
            if(cx<0||cy<0||cx>=n||cy>=m){
                if(f == 1){
                    continue;
                }
                else{
                    cout<< visit[y][x];
                    return;
                }
            }
            else{
                if(visit[cy][cx] != 0 || myMap[cy][cx] =='#'){
                    continue;
                }
                else{
                    q.push({cy,cx,f});
                    visit[cy][cx] = visit[y][x] + 1;
                }
            }
        }
    }
    cout << "IMPOSSIBLE";

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >>test_case;
    int sx,sy;
    for(int t = 0; t < test_case; t++){
        cin >> n >> m;
        memset(myMap,0,sizeof(myMap));
        memset(visit,0,sizeof(visit));
        while( !q.empty()){
            q.pop();
        }
        for(int i = 0 ; i < m ; i ++){
            for (int j = 0; j <n ; j++){
                cin >> myMap[i][j];
                if(myMap[i][j] == '@'){
                    sx = j;
                    sy = i;
                }
                else if(myMap[i][j] == '*'){
                    q.push({i,j,1});
                    visit[i][j] = 1;
                }
            }
        }
        q.push({sy,sx,0});
        visit[sy][sx] = 1;
        bfs();
        cout << '\n';
    }
}