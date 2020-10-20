#include <bits/stdc++.h>

using namespace std;

int mx [4] = {0,-1,0,1};
int my [4] = {-1,0,1,0};

int main(void){
	int n,m,count = 1;
	int startX,startY,dir,i,j;
	//scanf("%d %d\n",&n,&m);
	cin >> n >> m;
	cin >> startX >>startY >>dir;
	//scanf("%d %d %d",&startX, &startY, &dir);
	int map[n][m] = {0};
	int visitied[n][m] = {0};
	for(i = 0; i < n ; i ++){
		for(j = 0; j < n; j++){
			int tmp;
			cin >> tmp;
			map[i][j] = tmp;
		}
	}
	stack <int> ss;
	ss.push(startX);
	ss.push(startY);
	visitied[startX][startY] = 1;
	int ssx,ssy,x,y;
	//cout << "startX :" <<startX << " startY :" << startX<<'\n';
	while(!ss.empty()){
		ssx = ss.top();
		ss.pop();
		ssy = ss.top();
		ss.pop();
		for(i = dir; i < 4; i++){
			x = ssx + mx[i];
			y = ssy + my[i];
			//cout << "x :" <<x << " y :" << y<<'\n'<<'\n';
			if(x<0||y<0||x>n||y>m){
				continue;
			}
			else{
				if(map[x][y] == 0 && visitied[x][y] == 0){
					
					ss.push(x);
					ss.push(y);
					visitied[x][y] = 1;
					count ++;
					//cout << "xxxx :" <<x << " yyyy :" << y<<'\n';
				}
			}
		}
		int ddir = (i + 2) % 4;
		x = ssx + mx[ddir];
		y = ssy + my[ddir];
		if(x<0||y<0||x>n||y>m || map[x][y] ==1){
				break;
		}
		
	}
	cout << "count : " <<count;
	return 0;
}


	
