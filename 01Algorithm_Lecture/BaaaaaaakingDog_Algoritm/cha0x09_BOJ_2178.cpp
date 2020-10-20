#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;
int visit [101][101];
int myMap [101][101];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

int n , m;
int main(){
	int cx,cy;
	ios::sync_with_stdio(0);
	queue <pair <int , int> > q;
	scanf("%d %d", &n, &m);
	for(int i = 0; i < n ;i ++){
		for(int j = 0; j < m ; j++){
			scanf("%1d",&myMap[i][j]);
		}
	}
	q.push(make_pair(0,0));
	visit[0][0] = 1;
	int count = 1;
	for(int i = 0; i < n ;i ++){
		for(int j = 0; j < m ; j++){
			if(visit[i][j] == 1 || myMap[i][j] == 0){
				continue;
			}
			else{
				while(!q.empty()){
					if(cx == n -1 && cy == m - 1){
					break;
					}
					pair <int, int> current = q.front();
					q.pop();
					for(int dir = 0; dir <4 ; dir ++){
						cx = current.first + dx[dir];
						cy = current.second + dy[dir];
						if(cx<0|| cy<0|| cx >=n|| cy >=m){
							continue;
						}
						else if(visit[cx][cy] == 0 && myMap[cx][cy] == 1){
							q.push(make_pair(cx,cy));
							visit[cx][cy] = 1;
							myMap[cx][cy] = myMap[current.first][current.second] + 1;
						}
					}
				}
			}
		}
	}
	printf("%d",myMap[n-1][m-1]);
}
			
	
