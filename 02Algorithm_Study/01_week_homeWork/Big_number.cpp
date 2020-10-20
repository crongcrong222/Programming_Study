#include <string>
#include <vector>
#include <algorithm>

using namespace std;



bool compare(const string& a,const string& b){
    /*
    int len = min(a.size(),b.size());
    
    if(a.size() == b.size()){
        if(a[0] == b[0]){
        int tmpa = stoi(a);
        int tmpb = stoi(b);
        return tmpa>tmpb;
    }
        else{
            return a[0] > b[0];
        }
    }
    else{
        
    }
    */
    return a +b > b + a;
        
}
string solution(vector<int> numbers) {
    string answer = "";
    vector <string> vecstr;
    
    int len = numbers.size();
    
    for (int i = 0; i < len; i ++){
        string tmp = to_string(numbers[i]);
        vecstr.push_back(tmp);        
    }
    sort(vecstr.begin(),vecstr.end(),compare);
    
    for(int i = 0; i < vecstr.size(); i ++){
        answer += vecstr[i];
    }
    if(answer[0] == '0'){
        answer = '0';
    }
    
    return answer;
}