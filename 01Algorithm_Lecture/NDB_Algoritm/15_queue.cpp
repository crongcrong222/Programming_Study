#include <iostream>
#include <queue>

using namespace std;
int main(void){
	queue <int> q;
	q.push(7);
	q.push(6);
	q.pop();
	q.push(8);
	while(!q.empty()){
		cout << q.front() << '\n';
		q.pop();
	}
	return 0;
}
