#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector <int> che;
    int tmp[2] = {-1,1};
    for(int i = 0; i < n ; i ++){
        che.push_back(1);
    }
    
    for (int i = 0; i < lost.size(); i ++){
        che[lost[i]-1] -=1;
    }
    for (int i = 0; i < reserve.size(); i++){
        che[reserve[i]-1] +=1;
    }
    
    for (int i = 0; i < n; i ++){
        for (int j = 0; j<2; j ++){
            int give = i + tmp[j];
            if(give<0 or give>=n){
                continue;
            }
            else{
                if(che[give] == 2 && che[i] == 0){
                    che[give] -=1;
                    che[i]+=1;
                }
            }
        }
    }
    for (int i = 0; i <n; i ++){
        //printf("%d ",che[i]);
        //cout << che[i] << ' ';
        if(che[i]>0){
        answer ++;
        }
    }
    return answer;
}
