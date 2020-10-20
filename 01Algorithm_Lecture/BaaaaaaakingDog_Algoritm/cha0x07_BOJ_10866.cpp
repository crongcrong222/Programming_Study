#include <iostream>
#include <deque>


using namespace std;
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int n,tmp;
	cin >>n;
	string st;
	deque <int> dq;
	for(int i = 0; i < n ; i++){
		cin >>st;
		if(st =="push_front"){
			cin >>tmp;
			dq.push_front(tmp);
		}
		else if(st == "push_back"){
			cin>>tmp;
			dq.push_back(tmp);
		}
		else if(st == "front"){
			if(dq.empty()){
				cout << "-1\n";
			}
			else{
				cout << dq.front()<<'\n';
			}
		}
		else if(st =="back"){
			if(dq.empty()){
				cout << "-1\n";
			}
			else{
				cout << dq.back()<<'\n';
			}
		}
		else if(st == "pop_front"){
			if(dq.empty()){
				cout << "-1\n";
			}
			else{
				tmp = dq.front();
				dq.pop_front();
				cout << tmp <<'\n';
			}
		}
		else if(st == "pop_back"){
			if(dq.empty()){
				cout << "-1\n";
			}
			else{
				tmp = dq.back();
				dq.pop_back();
				cout << tmp <<'\n';
			}
		}
		else if(st == "size"){
			cout << dq.size() <<'\n';
		}
		else if(st =="empty"){
			if(dq.empty()){
				cout << "1\n";
			}
			else{
				cout << "0\n";
			}
		}
	}
}
			
			
	
