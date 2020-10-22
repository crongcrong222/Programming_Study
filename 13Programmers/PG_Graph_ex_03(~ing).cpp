//https://programmers.co.kr/learn/courses/30/lessons/49190
#include <string>
#include <vector>
#include <map>
using namespace std;

int dx[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};

int solution(vector<int> arrows) {
    int answer = 0;
    map<pair<int, int>, int> visited;
    // map »ç¿ë¹ý
	// https://jae1.tistory.com/5 
    map<pair<pair<int, int>, pair<int, int>>, int> check;
    
    
    int x = 0;
    int y = 0; 
    visited[{x,y}] = 1;
    for (int i = 0; i < arrows.size();i++){
    	for ( int j = 0; j < 2; j++){
    		int nx = x + dx[arrows[i]];
    		int ny = y + dy[arrows[i]];
    		if (visited[{nx,ny}] ==1 && check[{{x,y},{nx,ny}}] == 0){
    			answer ++;
    		}
    		visited[{nx,ny}] = 1;
    		
    		
    		check[{{x,y},{nx,ny}}] = 1;
    		check[{{nx,ny},{x,y}}] = 1;
    		x = nx;
    		y = ny;
    	}
    }
    return answer;
}
