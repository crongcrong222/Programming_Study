#include <bits/stdc++.h>

using namespace std;

struct rect{
	int sx,sy,ex,ey;
};

struct position{
	int y,x;
};
queue <position> q;
queue <rect> re;
int myMap[101][101];
int visit[101][101];
vector <int> size;
int m,n,k;

int dx[4] = {0,0,1,-1};
int dy[4] = {-1,1,0,0};

bool compare(int a,int b){
	return a<b;
}


int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> m >> n >> k;
	for(int i =0 ; i < k ; i++){
		int tmp1, tmp2, tmp3, tmp4;
		cin >> tmp1 >> tmp2 >> tmp3 >> tmp4;
		re.push({tmp1,tmp2,tmp3,tmp4});
	}
	int si = 0;
	while(!re.empty()){
		int sx = re.front().sx;
		int sy = re.front().sy;
		int ex = re.front().ex;
		int ey = re.front().ey;
		re.pop();
		for(int j = sy; j <ey;j++){
			for(int i = sx; i < ex; i++){
				myMap[j][i] = 1;
			}
		}

	}
	int rInx = 0;
	for(int j = 0; j <m; j ++){
		
		for(int i = 0; i < n; i++){
			if(myMap[j][i] == 0 && visit[j][i] == 0){
				q.push({j,i});
				visit[j][i] = 1;
				si = 0;

				
			}
			else{
				continue;
			}
			while(!q.empty()){
				int x = q.front().x;
				int y = q.front().y;
				q.pop();
				si ++;
				for(int dir = 0; dir < 4; dir ++){
					
					int cx = x + dx[dir];
					int cy = y + dy[dir];
					if(cx<0||cy<0||cx>=n||cy>=m){
						continue;
					}
					else{
						if(myMap[cy][cx] == 0 && visit[cy][cx] == 0){
							q.push({cy,cx});
							visit[cy][cx] = 1;
							
						}
					}
				}
			}
			size.push_back(si);
		}
	}

	sort(size.begin(),size.end());
	cout << size.size()<< '\n';
	for(int i = 0; i < size.size(); i++){
		cout << size[i] << ' ';
	}
	// cout << "rInx : " << rInx << '\n';
	// cout << "m : " <<m << '\n';
	// cout << "n : " <<n << '\n';
	// for(int j = 0; j <m; j ++){
	// 	for(int i = 0; i < n; i++){
	// 		cout << visit[j][i];
	// 	}
	// 	cout << '\n';
	// }
}
