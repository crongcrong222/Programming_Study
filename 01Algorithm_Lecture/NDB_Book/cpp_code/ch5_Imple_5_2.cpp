#include <bits/stdc++.h>

using namespace std;

int n,m;
int fff[201][201];
int mx[4] = {0,0,-1,+1};
int my[4] = {-1,+1,0,0};


int bfs(int x, int y){
	queue<pair<int, int> > q;
	q.push({x,y});
	
	while(!q.empty()){
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		
		for(int i = 0 ; i < 4; i ++){
			int nx = x + mx[i];
			int ny = y + my[i];
			if(nx<0||ny<0||nx>=n||ny>=m){
				continue;
			}
			if(fff[nx][ny] == 0){
				continue;
			}
			if(fff[nx][ny] == 1){
				fff[nx][ny] = fff[x][y] + 1;
				q.push({nx,ny});
			}
		}
	}
	return fff[n-1][m-1];
}

int main(void){
	cin >> n >> m;
	for (int i = 0; i < n ; i ++){
		for (int j = 0; j < m ; j++){
			scanf("%1d", &fff[i][j]);
		}
	}
	
	cout << bfs(0,0) << '\n';
	
	return 0;
}

