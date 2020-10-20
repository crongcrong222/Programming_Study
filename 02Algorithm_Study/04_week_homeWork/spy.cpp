#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;

    unordered_map <string, int> m;


    for( auto i : clothes){
        if(m.find(i[1]) == m.end()){
            m.insert(make_pair(i[1],1));
        }
        else{
            m.find(i[1]) ->second++;
        }
    }


    for(auto i = m.begin() ; i != m.end(); i++){
        answer = answer * (i->second + 1);

    }
    return answer - 1;
}