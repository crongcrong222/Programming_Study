#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<int, string> &a, const pair<int, string> &b){
	return a.first<b.first;
}
int main(){
	vector<pair<int, string> > v;
	v.push_back(pair<int, string>(90,"나동빈"));
	v.push_back(pair<int, string>(50,"차애리"));
	v.push_back(pair<int, string>(20,"박의준"));
	v.push_back(pair<int, string>(100,"서리안"));
	
	sort(v.begin(),v.end(),compare);
	for(int i = 0; i < v.size(); i ++){
		cout << v[i].second << ' ';
	}
	return 0;
}
