#include <bits/stdc++.h>

#define X first
#define Y second
using namespace std;



int main(void){
	int dx[4] = {-1,0,1,0};
	int dy[4] = {0,1,0,-1};
	
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int n,m;
	cin >>n >> m;
	vector <int> v;
	queue <pair<int, int> > q;
	int visit[502][502] = {0};
	int map[502][502] = {0};
	for(int i = 0; i < n; i ++){
		for(int j = 0; j < m ; j ++){
			cin >> map[i][j];
		}
	}
	int mx = 0,count = 0;
	for(int i = 0; i < n; i ++){
		for(int j = 0; j < m ; j ++){
			if(map[i][j] == 1 && visit[i][j] == 0){
				count ++;
				visit[i][j] = 1;
				q.push(make_pair(i,j));
				int area = 0;
				while(!q.empty()){
					area ++;
					pair <int, int> current = q.front();
					q.pop();
					
					for(int dir = 0; dir<4; dir ++){
						int cx = current.first + dx[dir];
						int cy = current.second + dy[dir];
						if(cx<0||cy <0|| cx>=n||cy>=m){
							continue;
						}
						else{
							if(visit[cx][cy] == 0 && map[cx][cy] ==1){
								visit[cx][cy] = 1;
								q.push(make_pair(cx,cy));
							
						}
					}
				}
				mx = max(mx,area);
			}
		}
	}
}
cout << count <<' ' <<mx<<'\n';
return 0;
}
