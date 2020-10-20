#include <bits/stdc++.h>

using namespace std;

int myMap[101][101];
int visit[101][101];
int dx[4] = {0,0,-1,1};
int dy[4] = {1,-1,0,0};

vector <int> rain;
int n;

void bfs(int h,int y, int x){

    queue <pair<int,int>> q;

    q.push(make_pair(y,x));
    visit[y][x] = 1;

    while(!q.empty()){
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int dir = 0; dir<4 ; dir++){
            int cy = y + dy[dir];
            int cx = x + dx[dir];
            if(cx<0||cy<0||cx>=n||cy>=n){
                continue;
            }
            else{
                if(visit[cy][cx] == 0 && myMap[cy][cx]>h){
                    visit[cy][cx] = 1;
                    q.push(make_pair(cy,cx));
                }
            }
        }
    }
}


bool compare(int a, int b){
    return a>b;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int maxx = 0;
    cin >>n;

    for (int i = 0; i < n ; i ++){
        for(int j = 0; j <n; j++){
            cin >>myMap[i][j]; 
            if (myMap[i][j] >maxx){
                maxx = myMap[i][j];
            }
        }
    }
    for(int k = 0; k <= maxx; k ++){
        int cnt = 0;
        memset(visit,0,sizeof(visit));
        for (int i = 0; i < n ; i ++){
            for(int j = 0; j <n; j++){
                
                
            
                if(myMap[i][j] > k && visit[i][j] ==0){
                    bfs(k,i,j);
                    cnt++;
                }
            }
        }
        rain.push_back(cnt);
    }
    sort(rain.begin(),rain.end(),compare);

    // for (int i = 0; i <=maxx ; i ++){
    //     cout<<rain[i] << ' ';
    // }
    // cout << '\n';



    cout << rain[0];
}