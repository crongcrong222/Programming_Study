#include <bits/stdc++.h>
using namespace std;


int main(void){
	int N, K,count = 0;
	cin >> N >> K;
	while(1){
		if(N ==1){
			break;
		}
		if(N%K == 0){
			N = N/K;
			count++;
		}
		else{
			N -=1;
			count++;
		}
	}
	cout << "count : " << count;
	return 0;
}

		
	
