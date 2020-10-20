//#include <iostream>
//#include <algorithm>
//using namespace std;
//bool compare(int a, int b){
//	return a<b;
//}
//
//int main(void){
//	int n,m,k;
//	int sum = 0;
//	int a[10001];
//	scanf("%d %d %d\n",&n,&m,&k);
//	for(int i = 0; i < n ; i ++){
//		scanf("%d",&a[i]);
//	}
//	sort(a, a + n,compare);
//	while(1){
//		for(int i = 0; i < k; i++){
//			if( m == 0 ){
//				break;
//			}
//			sum += a[n-1];;
//			m--;
//		}
//		if( m == 0 ) {
//			break;
//		}
//		sum += a[n-2];
//		m--;
//	}
//	cout << "sum : " << sum ;
//	return 0;
//}
//	


#include <bits/stdc++.h>

using namespace std;

int n, m, k;
vector <int> v;

int main(){
	cin >> n >> m >> k;
	
	for(int i = 0; i < n; i ++){
		int a;
		cin >> a;
		v.push_back(a);
	}
	
	sort(v.begin(), v.end());
	
	int firstN = v[n-1];
	int secondN = v[n-2];
	int sum = 0;
	while(1){
		for(int i = 0; i < k; i ++){
			if(m == 0){
				break;
			}
			sum += firstN;
			m--;
		}
		if(m==0){
			break;
		}
		sum += secondN;
		m--;
	}
	cout << "sum : " << sum;
	return 0;
}
	
