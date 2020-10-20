#include <iostream>
#include <stack>

using namespace std;

int main(void){
	stack <int> s;
	s.push(6);
	s.push(5);
	s.push(1);
	s.push(9);
	s.pop();
	s.push(3);
	
	while(!s.empty()){
		cout << s.top() <<'\n';
		s.pop();
	}
	return 0;
}
