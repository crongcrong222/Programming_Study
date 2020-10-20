#include <string>
#include <vector>
#include <queue>


using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int sum = 0;
    int i=0;
    queue<int> bridge;
    while(1){
    	if(i == truck_weights.size()){
    		answer += bridge_length;
    		break;
		}
    	answer++;
    	int tmp = truck_weights[i];
    	if(bridge.size() == bridge_length){
    		sum -= bridge.front();
    		bridge.pop();
    	}
    	
    	
    	if( tmp + sum <= weight){
    		bridge.push(tmp);
    		sum+=tmp;
    		i++;
    	}
    	
		else{
    		bridge.push(0);
    	}
    }
    return answer;
}
