 #include <iostream>
 #include <queue>
 using namespace std;
 int main(void){
 	ios::sync_with_stdio(0);
 	cin.tie(0);
 	cout.tie(0);
 	string st;
 	
 	int n,k;
 	cin >>n;
 	queue <int> q;
 	
 	for(int i = 0; i < n ; i ++){
 		cin >> st;
 		if(st == "push"){
 			cin >>k;
 			q.push(k);
 		}
 		else if(st == "pop"){
 			if(q.empty()){
 				cout << "-1\n";
 			}
 			else{
 				k = q.front();
 				q.pop();
 				cout << k << '\n';
 			}
 		}
 		else if(st=="size"){
 			cout << q.size() <<'\n';
 		}
 		else if(st=="empty"){
 			if(q.empty()){
 				cout <<"1\n";
 			}
 			else{
 				cout <<"0\n";
 			}
 		}
 		else if(st=="front"){
 			if(q.empty()){
 				cout <<"-1\n";
 			}
 			else{
 				k = q.front();
 				cout << k << '\n';
 			}
 		}
 		else if(st=="back"){
 			if(q.empty()){
 				cout <<"-1\n";
 			}
 			else{
 				k = q.back();
 				cout << k << '\n';
 			}
 		}
 	}
 	return 0;
 }
