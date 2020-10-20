#include <bits/stdc++.h>

using namespace std;

int myMap[302][302];
int bing[302][302];
int visit[302][302];
int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};
int n,m;

void bfs(int y, int x){

    queue <pair<int,int>> q;
    q.push(make_pair(y,x));
    visit[y][x] =1;
    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for(int dir= 0; dir<4; dir++){
            int cy = y + dy[dir];
            int cx = x + dx[dir];
            if(cx<0||cy<0||cx>=m||cy>=n){
                continue;
            }
            else{
                if(visit[cy][cx] == 0 && myMap[cy][cx] !=  0){
                    visit[cy][cx] = 1;
                    q.push(make_pair(cy,cx));
                }
            }
        }
    }
}

void check(int y, int x){
    int minus = 0;
    for(int dir= 0; dir<4; dir++){
        int cy = y + dy[dir];
        int cx = x + dx[dir];
        if(cx<0||cy<0||cx>=m||cy>=n){
                continue;
        }
        else{
            if(myMap[cy][cx] == 0){
                minus ++;
            }
        }
    }
    if(myMap[y][x] - minus <0){
        bing[y][x] = myMap[y][x];
    }
    else{
        bing[y][x] =minus;
    }

}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >>n >> m;

    for(int i = 0; i < n; i ++){
        for(int j = 0; j < m; j ++){
            cin >> myMap[i][j];
        }
    }
    
    
    int year = 0;
    while(1){
        int cnt = 0;
        int summ = 0;
        memset(visit,0,sizeof(visit));
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                if(visit[i][j] == 0 && myMap[i][j] != 0){
                    bfs(i,j);
                    cnt++;
                }
            }
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                
                if(myMap[i][j] !=0){
                    check(i,j);
                }
            }
        }
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                if(myMap[i][j] !=0){
                    myMap[i][j] -= bing[i][j];
                }
                summ +=myMap[i][j];
            }
        }
        // cout <<'\n';
        // for(int i = 0; i < n; i ++){
        //     for(int j = 0; j < m; j ++){
        //         cout <<myMap[i][j] <<' ';
        //     }
        //     cout <<'\n';
        // }
        
               
        if (cnt >= 2){
            //cout <<"ASDASDSAD"<<'\n';
            break;
        }
        if(summ == 0){
            year = 0;
            //cout <<"1111"<<'\n';
            break;
        }
        year++;
    }
    cout <<year;
}   