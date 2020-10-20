#include <bits/stdc++.h>

using namespace std;

int tmp[101][101];
int myMap[101][101];
int visit[101][101];
int dx[4] ={0,0,-1,1};
int dy[4] ={-1,1,0,0};
int n;

void number_island(int y, int x, int num){
    queue<pair<int,int>> qq;
    visit[y][x] = 1;
    myMap[y][x] = num;
    qq.push(make_pair(y,x));
    while(!qq.empty()){
        int y = qq.front().first;
        int x = qq.front().second;
        qq.pop();
        for(int dir = 0; dir < 4 ; dir++){
            int cy = y + dy[dir];
            int cx = x + dx[dir];
            if(cx<0||cy<0||cx>=n||cy>=n){
                continue;
            }
            else{
                if(visit[cy][cx] == 0 && tmp[cy][cx] == 1){
                    visit[cy][cx] = 1;
                    qq.push(make_pair(cy,cx));
                    myMap[cy][cx] = num;
                }
            }
        }
    }
}

// int bfs(int y, int x){
//     int bridge = myMap[y][x];
//     queue <pair <int,int>> q;
//     q.push(make_pair(y,x));
//     visit[y][x] = 0;
//     while(!q.empty()){
//         int y = q.front().first;
//         int x = q.front().second;
//         q.pop();
//         for(int dir = 0; dir < 4 ; dir ++){
//             int cy = y + dy[dir];
//             int cx = x + dx[dir];
//             if(cx<0||cy<0||cx>=n||cy>=n){
//                 continue;
//             }
//             else{
//                 if(myMap[cy][cx] == 0 && visit[cy][cx] == 0){
//                     q.push(make_pair(cy,cx));
//                     visit[cy][cx] = visit[y][x] + 1;
//                 }
//                 else if(myMap[cy][cx] != 0 && bridge != myMap[cy][cx]){
//                     visit[cy][cx] = 0;
//                     return visit[y][x];
//                 }
//             }
//         }
//     }
//     return 11111111;
// }

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >>n;
    
    for(int i = 0; i< n; i++){
        for(int j = 0; j <n; j++){
            cin >>tmp[i][j];
        }
    }
    int num = 0;
    for(int i = 0; i< n; i++){
        for(int j = 0; j <n; j++){
            if(tmp[i][j] == 1 && visit[i][j] == 0){
                num ++;
                number_island(i,j,num);
            }
        }
    }
    // cout << '\n';
    // cout << '\n';
    memset(visit,-1,sizeof(visit));
    // for(int i = 0; i< n; i++){
    //     for(int j = 0; j <n; j++){
    //         cout << visit[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }

    // int minn =9999999;
    // int mmin = 0;
    // for(int i = 0; i< n; i++){
    //     for(int j = 0; j <n; j++){
    //         if(myMap != 0 && visit[i][j] == 0){
                
    //             mmin = bfs(i,j);
    //             cout <<"mmin : "<<mmin<<'\n';
    //             minn = min(minn,mmin);
                
    //         }
    //     }
    // }

    for(int nnnn = 1; nnnn <= num ; nnnn++){
        queue<pair<int,int>>q;
        for(int i = 0; i< n; i++){
            for(int j = 0; j <n; j++){
                //visit[i][j] = -1;
                if(tmp[i][j] == 1){
                    visit[i][j] = 0;
                    q.push(make_pair(i,j));
                }
            }
        }

        while(!q.empty()){
            int y = q.front().first;
            int x = q.front().second;
            q.pop();
            for(int dir = 0; dir < 4; dir ++){
                int cy = y + dy[dir];
                int cx = x + dx[dir];
                if(cx<0||cy<0||cx>=n||cy>=n){
                    continue;
                }
                else{
                    if(visit[cy][cx] == -1){
                        q.push(make_pair(cy,cx));
                        visit[cy][cx] = visit[y][x] + 1;
                        myMap[cy][cx] = myMap[y][x];
                    }
                }
            }
        }
        
    }
    int answer = -1;
    for(int i = 0; i< n; i++){
        for(int j = 0; j <n; j++){
            int y = i;
            int x = j;
            for(int dir = 0; dir < 4; dir ++){
                int cy = y + dy[dir];
                int cx = x + dx[dir];
                if(cx<0||cy<0||cx>=n||cy>=n){
                    continue;
                }
                else{
                    if(myMap[y][x] != myMap[cy][cx]){
                        if(answer == -1 || answer > visit[cy][cx] + visit[y][x]){
                            answer = visit[cy][cx] + visit[y][x];
                        }
                    }
                }
            }
        }
    }
    // cout << '\n';
    // cout << '\n';
    // for(int i = 0; i< n; i++){
    //     for(int j = 0; j <n; j++){
    //         cout << visit[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }
    //minn = minn-1;
    cout << answer;


}