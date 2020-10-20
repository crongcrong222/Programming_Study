 #include <iostream>
 #include <vector>
 
 using namespace std;
 
 int number = 7;
 int visited [7] = {0};
 vector <int> a[8];
 
 void DFS(int x){
 	if(visited[x])return;
 	visited[x] = true;
 	cout << x << ' ';
 	for(int i = 0; i < a[x].size(); i++){
 		int y = a[x][i];
 		DFS(y);
 	}
 }
 
 
 int main(void){
 	a[1].push_back(2);
 	a[2].push_back(1);
 	
 	a[1].push_back(3);
 	a[3].push_back(1);
 	
 	a[2].push_back(3);
 	a[3].push_back(2);
 	
 	a[2].push_back(4);
 	a[4].push_back(2);
 	
 	a[2].push_back(5);
 	a[5].push_back(2);
 	DFS(1);
 	return 0;
 }
 
