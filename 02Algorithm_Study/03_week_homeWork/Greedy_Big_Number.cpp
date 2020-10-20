#include <string>
#include <vector>
 
using namespace std;
 
//string solution(string number, int k) {
//    string answer = "";
// 
//    int numSize = number.size() - k;
//    int start = 0;
//    for(int i=0; i<numSize; i++) {
//        char maxNum = number[start];
//        int maxIdx = start;
//        cout << "start : "<< start << '\n';
//        for(int j=start; j<=k+i; j++) {
//            if(maxNum < number[j]) {
//                maxNum = number[j];
//                maxIdx = j;
//            }
//        }
//        start = maxIdx + 1;
//        answer += maxNum;
//    }
// 
//    return answer;
//}

#include <string>
#include <vector>
 
using namespace std;
string solution(string number, int k){
	string answer = "";
	
	int size = number.size() - k;
	int start = 0;
	for(int i = 0 ; i< size; i ++){
		char CharNum = number[start];
		int NumMax = start;
		for(int j = start; j <= k + i ; j ++){
			if(CharNum<number[j]){
				CharNum = number[j];
				NumMax = j;
			}
		}
			start = NumMax + 1;
			answer += CharNum;
	}
	return answer;
}
