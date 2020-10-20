#include <bits/stdc++.h>
using namespace std;

int m,n;

int main(void){
	cin >> m >> n;
	vector <int> v[m];
	vector <int> vv;
	for(int i = 0; i < m ; i ++){
		for(int j = 0; j < n ; j++){
			int a;
			cin >>a;
			v[i].push_back(a);
		}
		sort(v[i].begin(),v[i].end());
		int min;
		min = v[i][0];
		vv.push_back(min);
	}
	sort(vv.begin(),vv.end());
	int max;
	max = vv[m-1];
	cout << "end : " << max;
	return 0;
}

	
	
