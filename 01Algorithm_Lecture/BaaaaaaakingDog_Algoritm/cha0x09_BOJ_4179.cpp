#include <bits/stdc++.h>

using namespace std;
int n,m,startX,startY;
struct fire{
	int x,y,f;
};
char myMap[1001][1001];
int visit[1001][1001];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
queue <fire> q;

void bfs(){
	q.push({startX,startY,0});
	visit[startX][startY] = 1;
	while(!q.empty()){
		int x = q.front().x;
		int y = q.front().y;
		int f = q.front().f;
		q.pop();
		for(int i = 0; i < 4; i ++){
			int cx = x + dx[i];
			int cy = y + dy[i];
			if(cx<0||cx >=n||cy <0||cy>=m){
				if(f == 1){
					continue;
				}
				else{
					cout << visit[x][y];
					return;
				}
			}
			if (visit[cx][cy] !=0 || myMap[cx][cy] == '#'){
				continue;
			}
			else{
				q.push({cx,cy,f});
				visit[cx][cy] = visit[x][y] + 1;
			}
		}
	}
	cout << "IMPOSSIBLE";
}






int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	queue<pair <int, int> > fireQ;
	queue<pair <int, int> > humanQ;
	
	cin >>n>>m;

	for(int i = 0; i < n ; i++){
		for (int j = 0; j <m; j++){
			visit[i][j] = 0;
			cin>> myMap[i][j];
			if(myMap[i][j] == 'J'){
				startX =  i;
				startY = j;
			}
			else if(myMap[i][j] == 'F'){
				q.push({i,j,1});
				visit[i][j] = 1;
			}
		}
	}
	bfs();
	return 0;
}
