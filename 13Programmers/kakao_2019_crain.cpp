//def solution(board, moves):
//    answer = 0
//    hight = len(board)
//    width = len(board[0])
//    box = [0]
//    for i in moves:
//        pick = -1
//        privous = box[-1]
//        for j in range(hight):
//            if(board[j][i-1] != 0):
//                pick = board[j][i-1]
//                board[j][i-1] = 0
//                box.append(pick)
//                break
//        
//        if(privous == pick):
//            box.pop()
//            answer += 1
//            box.pop()
//            answer += 1
//    
//    
//    return answer
    
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int hight = board.size();
    int width = board[0].size();
    vector <int> box;
    box.push_back(0);
    for( int i  = 0 ; i < moves.size(); i++){
    	int pick = -1;
    	int previous = box.back();
        int moveIn = moves[i];
    	for ( int j = 0; j < hight ; j++){
    		if(board[j][moveIn-1] !=0){
    			pick = board[j][moveIn-1];
    			board[j][moveIn-1] = 0;
    			box.push_back(pick);
    			break;
    		}
    	}
    	if(previous == pick){
    		box.pop_back();
    		answer ++;
    		box.pop_back();
    		answer ++;
    	}
    }
    	
    return answer;
}
