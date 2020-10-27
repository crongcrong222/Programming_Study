 #include <iostream>
 #include <vector>
 #include <queue>
 using namespace std;
 int dx[4] = {0,-1,0,1};
 int dy[4] = {1,0,-1,0};
 //https://rebas.kr/785
 //https://penglog.tistory.com/75
//https://www.acmicpc.net/problem/3190
 
 int myMap[101][101];
 queue <pair <int,int>> q;
 int t[101];
char tchar[101];
 int n,k,l;
 int x,y,time;
 int tx;
 
 void solve(){
 	myMap[x][y] = 2;
 	q.push({x,y});
 	int direction = 0;
	while(1){
		x = x +dx[direction];
		y = y + dy[direction];
		time++;
		if(x<0 ||y<0||x>=n||y>=n || myMap[x][y] ==2){
			cout<<time;
			return;
		}
		else{
			if(myMap[x][y] ==0){
				int ttx = q.front().first;
				int tty = q.front().second;
				myMap[ttx][tty] = 0;
				q.pop();
			}
			myMap[x][y] = 2;
			q.push({x,y});
			if(time == t[tx]){
				if(tchar[tx] == 'D'){
					direction = (direction +3)%4;
				}
				else{
					direction = (direction+1)%4;
				}
				tx++;
			}
			
		}
	}
}
int main(void){
	cin >> n>>k;
	for (int i = 0; i < k; i++){
		int tmpx, tmpy;
		cin >>tmpx>>tmpy;
		myMap[tmpx-1][tmpy-1] = 1;
	}
	cin >>l;
	for (int i = 0; i < l;i++){
		cin >>t[i]>>tchar[i];
	}
	solve();
	return 0;
}
