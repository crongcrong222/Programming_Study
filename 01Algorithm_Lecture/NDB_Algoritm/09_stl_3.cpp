#include <iostream>
#include <algorithm>

using namespace std;

class Student {
	public:
	string name;
	int score;
	Student(string name, int score){
		this->name = name;
		this->score = score;
	}
	bool operator < (Student &student){
		this->score < student.score;
	}
};
	

int main(){
	Student student[] = {
		Student("唱悼后",90),
		Student("唱1后",30),
		Student("唱2后",50),
		Student("唱3后",80),
		Student("唱4后",0),
		Student("唱5后",9),
	};
	sort(student, student + 6);
	for (int i = 0; i < 6 ; i++){
	cout << student[i].name << ' ';
	}
	return 0;
}

