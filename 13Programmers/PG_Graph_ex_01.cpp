#include <string>
#include <vector>    // std::vector
#include <algorithm> // std::count
#include <queue>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    vector <vector<int>> graph(n+1, vector <int>());
    vector <bool> visit(n + 1,false);
    vector <int> path(n + 1, 0);
    queue <int> q;
    //방문 여부를 체크하는 리스트 생성
    for (int i = 0 ; i < edge.size(); i++){
        graph[edge[i][0]].push_back(edge[i][1]);
        graph[edge[i][1]].push_back(edge[i][0]);
    }
    
    //방문 노드를 각각 추가함
    q.push(1);
    //처음 방문할 곳을 deque에 넣음
    visit[1] = true;
    while(!q.empty()){
        int tmp = q.front();
        q.pop();
        visit[tmp] = true;
        //방문을 하고(queue에서 꺼내고) 방문 체크를 함
        for (int i = 0; i < graph[tmp].size(); i++){
            //해당 방문한 그래프와 연결된 다른 그래프 숫자(노드)를 하나씩 꺼내서 확인
            if(visit[graph[tmp][i]] == false){
                //만약 해당 숫자(노드)를 방문하지 않았으면
                q.push(graph[tmp][i]);
                visit[graph[tmp][i]] = true;
                //방문 대기열(queue)에 추가하고 방문 여부를 체크
                path[graph[tmp][i]] =path[tmp] + 1;
                //해당 그래프 숫자(노드)에 방문 횟수를 증가시킴
            }
        }
    }
    sort(path.begin(),path.end());
    //sort는 algorithm 라이브러리에 있음
    int maxx = path.back();
    answer = count(path.begin(),path.end(),maxx);
    //해당 데이터가 몇 개인지 count
    return answer;
}



