#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
char myMap[32][32][32];
int visit[32][32][32];
int checked[31][31][31];
int dx[6] = {-1,1,0,0,0,0};
int dy[6] = {0,0,1,-1,0,0};
int dz[6] = {0,0,0,0,1,-1};
int l,r,c;
int sx,sy,sz;
int ex,ey,ez;
//queue를 다 돌 때까지 탈출하지 못하면 실패

queue <int> q;



int bfs(){
	visit[sx][sy][sz] = 1;
	int answer = -1;
	while(!q.empty()){
		int x = q.front();
		q.pop();
		int y = q.front();
		q.pop();
		int z = q.front();
		q.pop();
		checked[x][y][z] ++;
		for (int dir = 0; dir <6;dir++){
			int cx = x + dx[dir];
			int cy = y + dy[dir];
			int cz = z + dz[dir];
			if((cx<l && cy<r&& cz<c&& cx>=0 && cy>=0 &&cz>=0) && myMap[cx][cy][cz] =='.' && visit[cx][cy][cz]==0){
				visit[cx][cy][cz] = visit[x][y][z] + 1;
				q.push(cx);
				q.push(cy);
				q.push(cz);
			}
			if(cx == ex && cy ==ey && cz == ez){
				
				answer = visit[x][y][z];
				return answer;
			}
			
		}
		
	}
	return answer;
}
	
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	while(1){
		
		memset(myMap,'#',sizeof(myMap));
		memset(visit,0,sizeof(visit));
		int result = -1;
		cin >>l>>r>>c;
		if(l ==0 && r ==0 &&c ==0){
			return 0;
		}
		for (int i = 0 ; i<l; i++){
			for (int j = 0;j<r;j++){
				for (int k = 0; k < c; k++){
					char tmp;
					cin >>tmp;
					myMap[i][j][k] = tmp;
					if(tmp == '#'){
						visit[i][j][k] = -1;
					}
					if(tmp=='S'){
						q.push(i);
						q.push(j);
						q.push(k);
					}
					if(tmp=='E'){
						ex = i;
						ey = j;
						ez = k;
					}
					
				}
			}
		}
		result = bfs();
		if(result ==-1){
			cout<<"Trapped!\n";
		}
		else{
			cout<<"Escaped in "<<result<<"minute(s).\n";
		}
		
	}
	return 0;
}
	
