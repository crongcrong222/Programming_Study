#include <bits/stdc++.h>
using namespace std;

int n;
string lines;

int x = 1, y = 1;

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
char move[4] = {'L','R','U','D'};

int main(void){
	cin >>n;
	cin.ignore();
	getline(cin,lines);
	
	for(int i = 0; i < lines.size() ; i ++){
		char xx = lines[i];
		int nx = 0, ny = 0;
		for(int j = 0; j < 4 ; j++){
			if(xx == move[j]){
				nx = x + dx[j];
				ny = y + dy[j];
			}
		}
		if(nx < 1 ||nx >n ||ny < 1 || ny > n){
			continue;
		}
		x = nx;
		y = ny;
	}
	cout << x << ' ' << y;
	return 0;
}
