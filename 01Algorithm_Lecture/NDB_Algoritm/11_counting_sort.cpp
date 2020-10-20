#include <stdio.h>

int main(){
	int temp;
	int count[5] = {0};
	int array[30] = {1,2,3,5,1,
					1,2,3,5,1,
					1,2,3,5,1,
					1,2,3,5,1,
					1,2,3,5,4,
					1,2,3,5,1};
	for(int i = 0; i < 30; i++){
		count[array[i]-1]++;
	}
	for(int i = 0; i < 5; i++){
		printf("%d ", count[i]);
	}
	return 0;
}
	
