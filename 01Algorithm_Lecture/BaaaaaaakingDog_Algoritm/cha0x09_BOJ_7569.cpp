//#include <bits/stdc++.h>
//
//using namespace std;
//
//struct tomato{
//	int h,x,y;
//};
//
//int dh[3] = {0,-1,1};
//int dx[4] = {-1,1,0,0};
//int dy[4] = {0,0,-1,1};
//
//int main(void){
//	
//	ios::sync_with_stdio(0);
//	cin.tie(0);
//	
//	int g,m,n;
//	cin >>g>>m>>n;
//	
//	int myMap[g][101][101] = {0};
//	int	visit[g][101][101] = {0};
//	
//	queue <tomato> q;
//	
//	for(int i = 0; i < g; i ++){
//		for(int j = 0; j <m; j++){
//			for(int k = 0; k <n; k++){
//				cin >>myMap[i][j][k];
//				visit[i][j][k] = -1;
//				if(myMap[i][j][k] >0){
//					q.push({i,j,k});
//					visit[i][j][k] = 0;
//				}
//			}
//		}
//	}
//	
//	while(!q.empty()){
//		int h = q.front().h;
//		int x = q.front().x;
//		int y = q.front().y;
//		q.pop();
//		
//		
//		for(int i = 0; i < 3; i++){
//			for(int j = 0; j <4; j++){
//				int ch = h + dh[i];
//				int cx = x + dx[j];
//				int cy = y + dy[j];
//				
//				if(ch<0||cx<0||cy<0||ch>=g||cx>=m||cy>=n){
//					continue;
//				}
//				else{
//					if(myMap[ch][cx][cy] != -1 && visit[ch][cx][cy] == -1)	{
//						visit[ch][cx][cy] = visit[h][x][y] + 1;
//						q.push({ch,cx,cy});
//					}
//				}
//			}
//		}
//	}
//	
//	for(int i = 0; i < g; i ++){
//		for(int j = 0; j <m; j++){
//			for(int k = 0; k <n; k++){
//				
//				cout <<visit[i][j][k]<< ' ';
//			}
//			cout << '\n';
//		}
//		cout <<'\n';
//	}
//	
//	int max = 0;
//	for(int i = 0; i < g; i ++){
//		for(int j = 0; j <m; j++){
//			for(int k = 0; k <n; k++){
//				if(visit[i][j][k] == 0 && myMap[i][j][k] ==0){
//					cout << "-1";
//					return 0;
//				}
//				if(max < visit[i][j][k]){
//					max = visit[i][j][k];
//				}
//			}
//		}
//	}
//	cout << max;
//	return 0;
//}
//	
//	



#include <bits/stdc++.h>

using namespace std;
struct tomato{
	int x,y,z;
};

int myMap[102][102][102];
int visit[102][102][102];
int dz[6] = {0,0,0,0,1,-1};
int dx[6] = {0,0,-1,1,0,0};
int dy[6] = {-1,1,0,0,0,0};

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	queue <tomato> q;
	int h,n,m;
	
	
	cin >> m >> n >> h;

	for(int k = 0; k < h ; k ++){
		for(int i = 0; i < n ; i ++){
			for(int j = 0; j < m; j++){
				int tmp;
				cin >> tmp;
				myMap[k][i][j] = tmp;
				if(myMap[k][i][j] == 1 ){
					q.push({k,i,j});
					visit[k][i][j] = 0;
				}
			}
		}
	}		 
	
	while(!q.empty()){
		//cout<<"----------------\n";
//		for(int i = 0; i < n ; i++){
//			for (int j = 0; j <m; j++){
//				cout << visit[i][j] <<' ';
//			}
//			cout<<'\n';
//		}
	
		int x = q.front().x;
		int y = q.front().y;
		int z = q.front().z;
		q.pop();
		for(int dir = 0; dir < 6; dir++){
			int cz = z + dz[dir];
			int cx = x + dx[dir];
			int cy = y + dy[dir];
			if(cz<0||cx<0||cy<0||cz>=m||cx>=h||cy>=n){
				continue;
			}	
			if(myMap[cx][cy][cz] == 0 && visit[cx][cy][cz] == 0){
				visit[cx][cy][cz] = visit[x][y][z] + 1;
				q.push({cx,cy,cz});
				myMap[cx][cy][cz] = 1;
				
			}
		}
	}
		
//	cout << '\n';
//	cout << '\n';
//
//	for(int k = 0; k < h ; k ++){
//		for(int i = 0; i < n ; i ++){
//			for(int j = 0; j < m; j++){
//				cout << visit[k][i][j]<< ' ';
//			}
//			cout << '\n';
//		}
//	}		
	int max = 0;
	for(int k = 0; k < h ; k ++){
		for(int i = 0; i < n ; i ++){
			for(int j = 0; j < m; j++){
				if(visit[k][i][j] == 0 && myMap[k][i][j] == 0){
					cout <<"-1";
					return 0;
				}
				if(max <visit[k][i][j]){
					max = visit[k][i][j];
				}
			}
		}
	}
	cout << max;
	return 0;
}
