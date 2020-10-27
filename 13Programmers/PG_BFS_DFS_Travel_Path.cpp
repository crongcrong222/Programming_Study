#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;





vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;

    unordered_map<string, vector<string>> mapp;
    sort(tickets.begin(), tickets.end(), greater < vector<string> > ());
    for (int i = 0; i < tickets.size(); i ++){
    	mapp[tickets[i][0]].push_back(tickets[i][1]);
    }
    vector <string> v = vector<string> {"ICN"};
    
    while(!v.empty()){
    	string start = v.back();
    	if(mapp.find(start) == mapp.end() || mapp[start].size() == 0){
    		answer.push_back(start);
    		v.pop_back();
        }
		//갈 수 있는 곳이 없거나 다 방문했으면
		else{
			v.push_back(mapp[start].back());
			mapp[start].pop_back();
		}
	}
	reverse(answer.begin(),answer.end());
		 
	return answer;
}


