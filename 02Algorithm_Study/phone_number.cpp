#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    for(string s1 : phone_book){
        for(string s2 : phone_book){
            if(s1 == s2){
                continue;
            }
            if(s2.length() > s1.length()){
                if(s1 == s2.substr(0,s1.length())){
                    return false;
                }
            }
        }
    }

    return answer;
}