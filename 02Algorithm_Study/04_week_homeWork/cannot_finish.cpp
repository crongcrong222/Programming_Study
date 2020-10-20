#include <string>
#include <vector>
#include <unordered_map>



using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    unordered_map <string, int> ansHash;

    for(auto name : completion){
        if(ansHash.end() == ansHash.find(name)){
            ansHash[name] = 1;
        }
        else{
            ansHash[name] ++;
        }
    }

    for(auto name : participant){
        if(ansHash.end() == ansHash.find(name)){
            return name;
        }
        else{
            ansHash[name]--;
            if(ansHash[name] < 0){
                return name;
            }
        }
    }
}