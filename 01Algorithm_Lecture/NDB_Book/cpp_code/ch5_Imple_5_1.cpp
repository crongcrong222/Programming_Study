#include <bits/stdc++.h>

using namespace std;

int n ,m;
int visited[1000][1000];

bool dfs(int x, int y){
	if(x <0||y <0|| x>=n|| y >=m){
		return false;
	}
	if(visited[x][y] == 0){
		visited[x][y] = 1;
		dfs(x,y+1);
		dfs(x,y-1);
		dfs(x+1,y);
		dfs(x-1,y);
		return true;
	}
	return false;
}



int main(void){
	cin >> n >> m;
	for(int i =0; i < n ; i ++){
		for(int j = 0; j < m ; j++){
			scanf("%1d",&visited[i][j]);
			//printf("visited[i][j] : %d\n",visited[i][j]);
		}
	}
	
	int count = 0;
	
	for(int i =0; i < n ; i ++){
		for(int j = 0; j < m ; j++){
			if(dfs(i,j)){
				count ++;
			}
		}
	}
	
	cout << "count : " <<  count<<'\n';
	return 0;
}				

