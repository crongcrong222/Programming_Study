#include <iostream>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
	return a>b;
}

using namespace std;
int main(void){
	int a[10] = {9,3,42,3,2,1,6,1,21,1};
	sort(a,a+10,compare);
	for(int i = 0; i < 10; i ++){
		cout << a[i] << ' ';
	}
	cout << endl;
	return 0;
}

