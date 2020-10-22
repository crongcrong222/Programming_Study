#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector <bool>> updateResults(n+1,vector<bool>(n+1,false));

	
    //vector 사용법
	//https://security-nanglam.tistory.com/244 
	
	for (int i = 0; i <results.size(); i++){
		int winPeople = results[i][0];
		int losePeople = results[i][1];
		updateResults[winPeople][losePeople] = true;
	}
	//플로이드 와샬 알고리즘
	for (int second = 1; second <= n; second ++){
		for (int first = 1; first <= n; first ++){
			for (int third = 1; third <= n; third ++){
				if(updateResults[first][second] && updateResults[second][third]){
					updateResults[first][third] = true;
				}
			}
		}
	}
	
	for (int i = 1; i<= n; i++){
		int tmp = 0;
		for (int j = 1; j <=n ; j++){
			if(i == j){
				continue;
				// 본인과 경기하는 경우는 없음  
			}
			if(updateResults[i][j] || updateResults[j][i]){
				tmp ++;
			}
		}
		if(tmp ==n-1){
				//자기 자신 빼고 모든 사람과 대결한 경우(승패를 확실히 알 경우)
				answer ++;
			}
	}
	
			
			 
	
    return answer;
}
