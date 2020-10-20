#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair <string, pair<int,int> > a,
			 pair <string, pair<int,int> > b){
	if(a.second.first == b.second.first){
		return a.second.second > b.second.second;
	} else{
		return a.second.first > b.second.first;
	}
}


int main(){
	vector<pair<string, pair<int, int> > > v;
	v.push_back(pair<string, pair<int,int> >("������",pair<int,int>(90,19961222)));
	v.push_back(pair<string, pair<int,int> >("���ָ�",pair<int,int>(100,19910417)));
	v.push_back(pair<string, pair<int,int> >("������",pair<int,int>(100,19900701)));
	v.push_back(pair<string, pair<int,int> >("������",pair<int,int>(10,19910203)));
	
	
	sort(v.begin(),v.end(),compare);
	for(int i = 0; i < v.size(); i ++){
		cout << v[i].first << ' ';
	}
	return 0;
}
