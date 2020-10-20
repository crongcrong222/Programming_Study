#include <bits/stdc++.h>


using namespace std;





int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	int m,n,k;
	
	int myMap[51][51] = {0};
	int visit[51][51] = {0};
	int dx[4] = {-1,1,0,0};
	int dy[4] = {0,0,1,-1};

	queue <int> q;
	cin >> T;
	for(int tt = 0; tt<T; tt++){
		memset(myMap,0,sizeof(myMap));
		memset(visit,0,sizeof(visit));
		cin >> m >>n >> k;
		for(int i = 0; i < k; i++){
			int tx,ty;
			cin >> tx >> ty;
			myMap[ty][tx] = 1;
		}
		
		int count = 0;
		for(int i = 0; i <n; i++){
			for(int j = 0; j < m ; j++){
				if(myMap[i][j] == 1 && visit[i][j] ==0){
					q.push(i);
					q.push(j);
					visit[i][j] = 1;
					
					
					while(!q.empty()){
						int y = q.front();
						q.pop();
						int x = q.front();
						q.pop();
						for(int k = 0; k < 4; k++){
							int cx = x + dx[k];
							int cy = y + dy[k];
							if(cx<0||cx>=m||cy<0||cy>=n){
								continue;
							}
							if(myMap[cy][cx] == 1 && visit[cy][cx] == 0){
								q.push(cy);
								q.push(cx);
								visit[cy][cx] = 1;
							}
						}
					}
					count ++;
				}
				else{
					continue;
				}
				
			}
		}
		cout << count << '\n';
	}
	return 0;
}
	
