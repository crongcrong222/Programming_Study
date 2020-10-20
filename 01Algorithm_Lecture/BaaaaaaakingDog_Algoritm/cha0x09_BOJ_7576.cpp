#include <bits/stdc++.h>

using namespace std;

int myMap[1001][1001];
int visit[1001][1001];
int n,m;
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};


int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	queue <pair <int, int> > q;
	
	cin >>m>>n;
	for(int i = 0; i < n ; i ++){
		for(int j = 0; j < m; j++){
			int tmp;
			cin >> tmp;
			myMap[i][j] = tmp;
			visit[i][j] = -1;
			if(myMap[i][j] > 0){
				q.push(make_pair(i,j));
				visit[i][j] = 0;
			}
		}
	}

	while(!q.empty()){
		cout<<"----------------\n";
		for(int i = 0; i < n ; i++){
			for (int j = 0; j <m; j++){
				cout << visit[i][j] <<' ';
			}
			cout<<'\n';
		}
		pair <int , int> current = q.front();
		q.pop();
		for(int dir = 0; dir < 4; dir++){
			int cx = current.first + dx[dir];
			int cy = current.second + dy[dir];
			if(myMap[cx][cy] != -1 && visit[cx][cy] == -1){
				visit[cx][cy] = visit[current.first][current.second] + 1;
				q.push(make_pair(cx,cy));
			}
		}
	}
	int max = 0;
	for(int i = 0; i< n; i ++){
		for(int j = 0; j<m; j++){
			if(visit[i][j] == -1 && myMap[i][j] == 0){
				cout <<"-1";
				return 0;
			}
			if(max <visit[i][j]){
				max = visit[i][j];
			}
		}
	}
	cout << max;
	return 0;
}
