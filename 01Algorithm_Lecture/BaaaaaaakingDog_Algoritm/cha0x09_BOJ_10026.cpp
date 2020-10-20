#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

char myMap[101][101];
int visit[101][101];
int n;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
struct position{
    int y,x;
};

void bfs(int y, int x, int redgreen){

    queue <position> q;
    char tmp = myMap[y][x];

    q.push({y,x});
    visit[y][x] = 1;
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        for(int dir = 0; dir< n; dir++){
            int cx = x + dx[dir];
            int cy = y + dy[dir];
            if(cx<0||cy<0||cx>=n||cy>=n){
                continue;
            }
            else{
                if(redgreen == 0){
                    if(visit[cy][cx] == 0 && myMap[cy][cx] == tmp){
                        visit[cy][cx] = 1;
                        q.push({cy,cx});
                    }
                }
                else if(redgreen == 1){
                   if(tmp == 'R' || tmp == 'G'){
                        if(visit[cy][cx] == 0 && (myMap[cy][cx] == 'R'|| myMap[cy][cx] == 'G')){
                            visit[cy][cx] = 1;
                            q.push({cy,cx});
                        }
                    }
                    else if(tmp == 'B'){
                        if(visit[cy][cx] == 0 && (myMap[cy][cx] == tmp)){
                            visit[cy][cx] = 1;
                            q.push({cy,cx});
                        }
                    }
                }
            }
        }
    }
}




int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int cnt = 0;
    int cnt2 = 0;
    cin >>n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            char tmp;
            cin>>tmp;
            myMap[i][j] = tmp;
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(visit[i][j] == 0){
                
                bfs(i,j,0);
                cnt++;
            }
        }
    }
    cout << cnt <<' ';
    memset(visit,0,sizeof(visit));

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(visit[i][j] == 0){
                
                bfs(i,j,1);
                cnt2++;
            }
        }
    }
        cout << cnt2;
        return 0;
}
