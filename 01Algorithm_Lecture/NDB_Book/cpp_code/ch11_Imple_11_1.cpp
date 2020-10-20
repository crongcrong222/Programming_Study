#include <bits/stdc++.h>


using namespace std;
int main(void){
	int n;
	cin >> n;
	vector <int> gild;
	int count = 0,result = 0;
	
	for (int i = 0; i < n ; i ++){
		int tmp;
		cin >> tmp;
		gild.push_back(tmp);
	}
	sort(gild.begin(),gild.end());
	int group = 0;
	int i = 0;
	for (int i = 0; i < n ; i++){
		count ++;
		if(count>=gild[i]){
			result += 1;
			count = 0;
		}
	}
	
	
	cout << result;
	return 0;
}
