 #include <iostream>
 using namespace std;
 int a[10001] ={0};
 int n;
 
 int main(void){
 	cin >> n;
 	for(int i = 0; i < n ; i++){
 		int x;
 		scanf("%d",&x);
 		a[x]++;
 	}
 	for(int i = 0; i < 10001 ; i++){
 		while (a[i] != 0){
 			cout << i <<'\n';
 			a[i]--;
 		}
 	}
 	return 0;
 }
