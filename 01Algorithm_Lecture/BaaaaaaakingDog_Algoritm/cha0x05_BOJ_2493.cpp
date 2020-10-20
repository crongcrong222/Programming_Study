#include <iostream>
#include <stack>
#include <algorithm>
#include <vector>

using namespace std;


int main(void){
	int n,tmp;
	cin >> n;
	stack <pair <int, int> > s;
	vector <int> v;
	for (int i = 1; i <=n ; i++){
		cin >> tmp;
		
		while(!s.empty()){
			if(s.top().second >=tmp){
				v.push_back(s.top().first);
				break;
			}
			s.pop();
				
		}
		if(s.empty()){
			v.push_back(0);
		}
		s.push(make_pair(i,tmp));
		
	}

	for(int i = 0; i < n ; i ++){
		cout << v[i] << ' ';
	}
	return 0;
}

		
			
