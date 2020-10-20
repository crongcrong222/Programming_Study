#include <string>
#include <vector>
#include <queue>


using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    for(int i = 0; i < prices.size(); i++){
        int result = 0;
        for(int j = i + 1; j < prices.size(); j++){
        	if(prices[j]>=prices[i]){
        		result ++;
        	}
        	else{
        		result++;
        		break;
            }
        }
        answer.push_back(result);
    }
    return answer;
}
