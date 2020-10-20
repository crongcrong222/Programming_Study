#include <iostream>
#include <stack>

using namespace std;

int main(void){
	stack <int> myS;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int tmp;
		cin >> tmp;
		
		if(tmp == 0){
			myS.pop();
			cout << "asdasdasd"<<'\n';
		}
		else{
			myS.push(tmp);
		}
	}
	int sum = 0,tt;
	while(!myS.empty()){
		tt = myS.top();
		cout << tt << '\n';
		
		sum +=tt;
		myS.pop();
	}
	cout << sum;
	return 0;
}

			
			
