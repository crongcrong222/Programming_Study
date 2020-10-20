#include <iostream>
#include <set>
#include <vector>
using namespace std;


int T,n,s;


int solution(int number, vector<int> student){

	int cnt = 0;
	int stuNum;
	for(int i = 0 ; i < student.size(); i++){
		set <int> s;
		stuNum = i + 1;
		
		
		while(1){
			int previous = s.size();
			s.insert(student[stuNum-1]);
			int nextstuNum = student[stuNum-1];
			//cout << "stuNum : " << stuNum << " student[stuNum-1] : "<< student[stuNum-1] <<'\n';
			//cout << "nextstuNum : " << nextstuNum <<" student[nextstuNum-1] : " << student[nextstuNum-1]<<'\n';
			s.insert(student[nextstuNum-1]);
			int present = s.size();
			stuNum = nextstuNum;
			set <int>::iterator j;
			// for(j = s.begin(); j!= s.end(); j++){
			// 	cout << *j << ' ';
			// }
			//cout << '\n';
			//cout << "previous : " << previous << " present  : "<< present << '\n';
			//cout << '\n';
			if(previous == present){
				break;
			}
		}
		stuNum = i + 1;
		if(s.count(stuNum) == 0){
			
			cnt ++;
		}
		s.clear();

	}
	return cnt;
}



int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin>>T;
	for(int t = 0; t<T; t++){

		vector <int> stu;
		cin>>n;
		
		for(int i =0; i <n; i++){
			int tmp;
			cin >> tmp;
			stu.push_back(tmp);
		}
		int answer = solution(n,stu);
		cout << answer <<'\n';
	}
}
