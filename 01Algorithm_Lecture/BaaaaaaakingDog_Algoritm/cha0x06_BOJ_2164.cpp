#include <iostream>
#include <queue>

using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int n;
	cin>>n;
	queue <int> q;
	for(int i = 0; i <n ;i++){
		q.push(i+1);
	}
	while(q.size()>1){
		q.pop();
		int k = q.front();
		q.pop();
		q.push(k);
	}
	cout << q.front();
}
	
