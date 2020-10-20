#include <bits/stdc++.h>
using namespace std;

int horizontal[8] = {-2,-2,2,2,-1,-1,1,1};
int vertical[8] = {1,-1,1,-1,2,-2,2,-2};

int main(void){
	char vv;
	int hh,xx,yy,count = 0;
	scanf("%c%d",&vv,&hh);
	int x = 0, y = 0;
	
	
	int dx = 0, dy = 0;
	for (int i = 0; i < 8 ; i ++){
		x = vv - 'a';
		y =hh - 1;
		cout << "xx : " << x << " yy : " << y << '\n';
		x = x + horizontal[i];
		y = y + vertical[i];
		if(x < 0 || x > 8 || y < 0 || y > 8){
			continue;
		}
		else{
			cout << "x : " << x << "y : " << y << '\n';
			count ++;
		}
	}
	cout << "count : " << count ;
	return 0;
}

		
