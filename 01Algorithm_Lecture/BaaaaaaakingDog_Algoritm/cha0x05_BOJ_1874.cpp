 #include <iostream>
 #include <stack>
 #include <vector>
 
 
 using namespace std;
 int main(void){
 	
 	int n,i,k = 0 ;
 	cin >> n;
 	stack <int> s;
 	vector <int> tt;
 	vector <char> v;
 	
 	for(i = 0; i < n ; i++){
 		int tmp;
 		cin >> tmp;
 		tt.push_back(tmp);
 	}
 	
 	for( i = 1; i <=n ; i ++){
 		s.push(i);
 		v.push_back('+');
 		while(!s.empty() && s.top() == tt[k]){
 			s.pop();
 			v.push_back('-');
 			k++;
 		}
 	}
 	if(!s.empty()){
 		cout << "NO\n";
 	}
 	else{
 		for(i = 0; i < v.size(); i++){
 			cout << v[i]<<'\n';
 		}
 	}
 	return 0;
 }
