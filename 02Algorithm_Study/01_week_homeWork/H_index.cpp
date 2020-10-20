#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int len = citations.size();
    int h_index = 0;
    sort(citations.begin(),citations.end());
    for(int i = 0; i < len ; i ++){
        int count = 0;
        for(int j = i + 1 ; j < len; j++){
            count ++;
        }
        if(count>citations[i]){
            h_index = count;
        }
    }
    answer = h_index;
    return answer;
}


int main(){
	vector <int> v;
	for(int i = 0; i < 5; i++){
		int tmp;
		cin >> tmp;
		v.push_vack(tmp);
	}
	solution(v);
}
