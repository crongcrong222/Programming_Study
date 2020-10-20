#include <bits/stdc++.h>

using namespace std;
int main(void){
	int n,data;
	cin >> n;
	stack <int> v;
	string ss = "";
	for(int i = 0; i <n ;i ++){
		cin >> ss;
		if(ss=="push"){
			cin >> data;
			v.push(data);
		}
		else if(ss=="top"){
			if(v.empty()){
				cout << "-1" <<'\n';
			}
			else{
				int tmp = v.top();
				cout << tmp <<'\n';
			}
		}
		else if(ss=="size"){
			cout << v.size() <<'\n';
		}
		else if(ss=="pop"){
			if(v.empty()){
				cout << "-1"<<'\n';
			}
			else{
				int tmp = v.top();
				cout << tmp <<'\n';
				v.pop();
			}
		}
		else if(ss=="empty"){
			if(v.empty()){
				cout << "1"<<'\n';
			}
			else{
				cout << "0"<<'\n';
			}
		}
	}
	return 0;
}
