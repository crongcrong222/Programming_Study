#include <iostream>
#include <queue>
#include <cstring>

using namespace std;


int dx[8] = {-1,-2,-2,-1,1,2,2,1};
int dy[8] = {2,1,-1,-2,-2,-1,1,2};
int n,l;
int myMap[301][301];
int visit[301][301];

struct position{
    int x,y;
};

void bfs(int l,int sx,int sy, int ex, int ey){
    queue <position> q;
    q.push({sx,sy});
    visit[sx][sy]=1;
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        q.pop();
        if(x == ex && y == ey){
                break;
            }
        for(int dir = 0; dir < 8; dir++){
            int cx = x + dx[dir];
            int cy = y + dy[dir];
            
            if(cx<0||cy<0||cx>=l||cy>=l){
                continue;
            }
            else{
                if(visit[cx][cy] == 0){
                    myMap[cx][cy] = myMap[x][y] + 1;
                    q.push({cx,cy});
                    visit[cx][cy]=1;
                }
            }
        }
    }

    // for(int i = 0 ; i <l; i++){
    //     for(int j = 0; j < l; j++){
    //         cout <<myMap[i][j] << ' ';
    //     }
    //     cout <<'\n';
    // }
    cout << myMap[ex][ey]<<'\n';
    //cout << myMap[ey][ex]<<'\n';
    return;
}


int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 0 ; i <n; i++){
        memset(visit,0,sizeof(visit));
        memset(myMap,0,sizeof(myMap));
        cin >> l;
        int sx,sy;
        cin >>sx>>sy;
        int ex,ey;
        cin >> ex>>ey;
        bfs(l,sx,sy,ex,ey);
    }
}
