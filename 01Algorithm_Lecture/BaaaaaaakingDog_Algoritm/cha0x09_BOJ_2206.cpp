#include <bits/stdc++.h>

using namespace std;

int myMap[1001][1001];
int visit[1001][1001][2];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
int n,m;
//visit에 벽 부순 횟수를 추가함

// 1. 이동하고자 하는 다음 칸이 1이고, 이미 벽을 부셨으면?
// -> 이동할 수 없고 queue에 넣지 않음
// 2. 이동하고자 하는 다음 칸이 1이고, 아직 벽을 안부셨으면?
// -> 벽 부순 표시를 하고, queue에 넣어 다음 칸 진행
// 3. 이동하고자 하는 다음 칸이 빈 칸이고, 벽을 부수고 방문한다면?
// -> 벽을 부수고 방문한 칸인지 확인하고, 아니면 queue에 넣어서 다음 단계 진행
// 4. 이동하고자 하는 다음 칸이 빈 칸이고, 벽을 부수지 않고 방문한다면?
// -> 벽을 부수지 않고 방문한 칸인지 확인하고, 아니면 queue에 넣어서 다음 단계 진행



int bfs(){
    queue <pair<pair<int,int>,int>> q;
    q.push(make_pair(make_pair(0,0),1));

    visit[0][0][1] = 1;

    while(!q.empty()){
        int x = q.front().first.second;
        int y = q.front().first.first;
        int B = q.front().second;

        q.pop();

        if(x == m-1 && y == n-1){
            return visit[y][x][B];
        }

        for(int dir = 0; dir<4; dir++){

            int cx = x + dx[dir];
            int cy = y + dy[dir];

            if(cx<0||cy<0||cx>=m||cy>=n){
                continue;
            }
            else{
                if(myMap[cy][cx] == 1 && B == 1){
                    visit[cy][cx][B-1] = visit[y][x][B] + 1;
                    q.push(make_pair(make_pair(cy,cx),B-1));
                }
                if(myMap[cy][cx] == 0 && visit[cy][cx][B] == 0){
                    visit[cy][cx][B] = visit[y][x][B] + 1;
                    q.push(make_pair(make_pair(cy,cx),B));
                }
            }
        }
    }
    return -1;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n>>m;

    for (int i = 0; i < n; i ++){
        for(int j = 0 ; j < m; j++){
            char a;
            cin >>a;
            myMap[i][j] = a - '0';
        }
    }
    cout << bfs()<< '\n';
    //  for (int i = 0; i < n; i ++){
    //     for(int j = 0 ; j < m; j++){
    //         cout << visit[i][j][0] <<' ';
    //     }
    //     cout << '\n';
    //  }
    
}