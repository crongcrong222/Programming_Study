 #include <iostream>
 #include <algorithm>
 #include <queue>
 #include <vector>
 
 
 using namespace std;
 
 int number = 6 ;
 int visited[6] = {0};
 vector<int> a[8];
 
 
 void BFS(int start){
 	queue <int> q;
 	q.push(start);
 	visited[start] = true;
 	while(!q.empty()){
 		int x = q.front();
 		q.pop();
 		printf("%d ",x);
 		for (int i = 0; i < a[x].size(); i++){
 			int y= a[x][i];
 			if(!visited[y]){
 				q.push(y);
 				visited[y] = true;
 			}
 		}
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
 	
	BFS(1);
	return 0;
}
 	
