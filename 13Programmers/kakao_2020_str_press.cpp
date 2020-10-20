#include <bits/stdc++.h>

using namespace std;

int solution(string s){
	int leng = s.size();
	int answer = leng;
	
	for ( int i = 1; i <=(leng/2); i++){
		string result = "";
		string tmp = s.substr(0,i);
		int count = 1;
		
		for(int j = i ; j <=leng ;j +=i){
			if(tmp == s.substr(j,i)){
				count ++;
			}
			else{
				if(count == 1){
					result += tmp;
				}
				else{
					result +=(to_string(count)+tmp);
				}
				
				tmp = s.substr(j,i);
				count = 1;
			}
		}
		result += s.substr((leng/i)*i);
		answer = min(answer,(int)result.length());
		
	}
	return answer;
}

