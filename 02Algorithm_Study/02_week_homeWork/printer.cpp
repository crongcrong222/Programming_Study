

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue <int> q;
    queue <pair <int,int> >arr;
    int idx = 0;
    for(int i = 0 ; i <priorities.size(); i++){
    	q.push(priorities[i]);
    	arr.push(make_pair(priorities[i],i));
    }
    
    while(1){
    	int pri = arr.front().first;
    	int order = arr.front().second;
    	arr.pop();
    	
    	if(pri == q.top()){
    		q.pop();
    		answer ++;
    		if(order == location){
    			break;
    		}
    	}
    	else{
    		arr.push(make_pair(pri,order));
    	}
    }
    
    		
    return answer;
}
