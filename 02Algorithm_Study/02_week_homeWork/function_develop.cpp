#include <string>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue <int> pro,spd;
    
    int day = 0;
    int tmp = 0
    while(tmp !=progresses.size()){
    	day++;
    	int complete = 0;
    	for(int i = tmp; i < progresses.size(); i++){
    		if(progresses[tmp] + day*speeds[tmp] >=100){
    			tmp++;
    			complete ++;
    		}
    	}
    	if(complete !=0){
    		answer.push_back(complete);
    	}
    }
    
    
    return answer;
}
