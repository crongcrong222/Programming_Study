#include <iostream>
#include <deque>
#include <queue>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	queue <int> q;
	int n,tmp,front;
	deque <int> deq;
	cin >>n;
	int m;
	cin >>m;
	deque<int>::iterator it;
	
	for(int i = 1; i <= n ; i ++){
		deq.push_back(i);
	}
	for(int i = 0; i <m; i++){
		cin>>tmp;
		q.push(tmp);
	}
	int count = 0;
	while(!q.empty()){
		tmp = q.front();
		q.pop();
		if(tmp == deq.front()){
			deq.pop_front();
			continue;
		}
		else{
			int index = 1;
			for(it = deq.begin(); it < deq.end(); it++){
				if(*it == tmp){
					break;
				}
				index ++;
			}
			int left = index - 1;
			int right = deq.size() + 1 -index;
			if(left<right){
				while(1){
					if(tmp == deq.front()){
						deq.pop_front();
						break;
					}
					else{
						int ttt;
						ttt = deq.front();
						deq.pop_front();
						deq.push_back(ttt);
						count++;
					}
				}
			}
			else{
				while(1){
					if(tmp == deq.front()){
						deq.pop_front();
						break;
					}
					else{
						int ttt;
						ttt = deq.back();
						deq.pop_back();
						deq.push_front(ttt);
						count++;
					}
				}
			}
		}
	}
	cout << count;
	return 0;
}

