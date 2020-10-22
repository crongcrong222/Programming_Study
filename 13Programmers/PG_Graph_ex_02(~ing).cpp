#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector <bool>> updateResults(n+1,vector<bool>(n+1,false));

	
    //vector ����
	//https://security-nanglam.tistory.com/244 
	
	for (int i = 0; i <results.size(); i++){
		int winPeople = results[i][0];
		int losePeople = results[i][1];
		updateResults[winPeople][losePeople] = true;
	}
	//�÷��̵� �ͼ� �˰���
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
				// ���ΰ� ����ϴ� ���� ����  
			}
			if(updateResults[i][j] || updateResults[j][i]){
				tmp ++;
			}
		}
		if(tmp ==n-1){
				//�ڱ� �ڽ� ���� ��� ����� ����� ���(���и� Ȯ���� �� ���)
				answer ++;
			}
	}
	
			
			 
	
    return answer;
}
