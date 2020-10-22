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
    //�湮 ���θ� üũ�ϴ� ����Ʈ ����
    for (int i = 0 ; i < edge.size(); i++){
        graph[edge[i][0]].push_back(edge[i][1]);
        graph[edge[i][1]].push_back(edge[i][0]);
    }
    
    //�湮 ��带 ���� �߰���
    q.push(1);
    //ó�� �湮�� ���� deque�� ����
    visit[1] = true;
    while(!q.empty()){
        int tmp = q.front();
        q.pop();
        visit[tmp] = true;
        //�湮�� �ϰ�(queue���� ������) �湮 üũ�� ��
        for (int i = 0; i < graph[tmp].size(); i++){
            //�ش� �湮�� �׷����� ����� �ٸ� �׷��� ����(���)�� �ϳ��� ������ Ȯ��
            if(visit[graph[tmp][i]] == false){
                //���� �ش� ����(���)�� �湮���� �ʾ�����
                q.push(graph[tmp][i]);
                visit[graph[tmp][i]] = true;
                //�湮 ��⿭(queue)�� �߰��ϰ� �湮 ���θ� üũ
                path[graph[tmp][i]] =path[tmp] + 1;
                //�ش� �׷��� ����(���)�� �湮 Ƚ���� ������Ŵ
            }
        }
    }
    sort(path.begin(),path.end());
    //sort�� algorithm ���̺귯���� ����
    int maxx = path.back();
    answer = count(path.begin(),path.end(),maxx);
    //�ش� �����Ͱ� �� ������ count
    return answer;
}



