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
		Student("������",90),
		Student("��1��",30),
		Student("��2��",50),
		Student("��3��",80),
		Student("��4��",0),
		Student("��5��",9),
	};
	sort(student, student + 6);
	for (int i = 0; i < 6 ; i++){
	cout << student[i].name << ' ';
	}
	return 0;
}

