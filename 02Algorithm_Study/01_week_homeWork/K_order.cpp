#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    int count = commands.size();
    
    for(int i = 0; i < count; i ++){
        vector <int> vecTmp;
        for(int j = commands[i][0] - 1; j < commands[i][1]; j ++){
            int tmp = array[j];
            vecTmp.push_back(tmp);
        }
        sort(vecTmp.begin(),vecTmp.end());
        answer.push_back(vecTmp[commands[i][2] - 1]);
    }
    
    return answer;
}
