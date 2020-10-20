#include <bits/stdc++.h>

using namespace std;

int myMap[1001][1001];
int visit[1001][1001][2];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
int n,m;
//visit�� �� �μ� Ƚ���� �߰���

// 1. �̵��ϰ��� �ϴ� ���� ĭ�� 1�̰�, �̹� ���� �μ�����?
// -> �̵��� �� ���� queue�� ���� ����
// 2. �̵��ϰ��� �ϴ� ���� ĭ�� 1�̰�, ���� ���� �Ⱥμ�����?
// -> �� �μ� ǥ�ø� �ϰ�, queue�� �־� ���� ĭ ����
// 3. �̵��ϰ��� �ϴ� ���� ĭ�� �� ĭ�̰�, ���� �μ��� �湮�Ѵٸ�?
// -> ���� �μ��� �湮�� ĭ���� Ȯ���ϰ�, �ƴϸ� queue�� �־ ���� �ܰ� ����
// 4. �̵��ϰ��� �ϴ� ���� ĭ�� �� ĭ�̰�, ���� �μ��� �ʰ� �湮�Ѵٸ�?
// -> ���� �μ��� �ʰ� �湮�� ĭ���� Ȯ���ϰ�, �ƴϸ� queue�� �־ ���� �ܰ� ����



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