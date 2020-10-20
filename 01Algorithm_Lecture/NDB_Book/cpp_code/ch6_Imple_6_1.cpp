#include <bits/stdc++.h>
using namespace std;

bool compare (int a, int b){
	return a>b;
}

int n,m;
int main(void){
	int tmp;
	cin >> n >> m;
	vector <int> a;
	vector <int> b;
	for(int i = 0; i < n ; i ++){
		scanf("%d",&tmp);
		a.push_back(tmp);
	}
	for(int i = 0; i < n ; i ++){
		scanf("%d",&tmp);
		b.push_back(tmp);
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end(),compare);
	for(int i = 0; i < m; i++){
		if(a[i] < b[i]){
			tmp = a[i];
			a[i] = b[i];
			b[i] = tmp;
		}
	}
	int result = 0;
	for ( int i = 0; i < n; i ++){
		result += a[i];
	}
	
	cout << result ;
	return 0;
}
