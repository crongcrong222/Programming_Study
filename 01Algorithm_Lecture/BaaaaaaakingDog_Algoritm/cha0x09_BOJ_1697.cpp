#include <bits/stdc++.h>

using namespace std;

#define Max 100001
int visit[Max];
int n,m;

int bfs(int n, int m){
	
	int count = 0;
	queue <int> q;
	q.push(n);
	while(1){
		int size = q.size();
		for (int i = 0; i < size; i++){
			int su = q.front();
			q.pop();
			if(su == m){
				return count;
			}
			if(su > 0 && visit[su-1] == 0){
				q.push(su-1);
				visit[su-1] = 1;
			}
			if(su <100000 && visit[su+1] == 0){
				q.push(su+1);
				visit[su+1] =1;
			}
			if(su * 2 <= 100000 && visit[su*2] == 0){
				q.push(su*2);
				visit[su*2] =1;
			}
		}
		count ++;
	}
}



int main(){
	cin >>n >> m;
	cout << bfs(n,m);
}
	
