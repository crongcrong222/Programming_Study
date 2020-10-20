 #include <stdio.h>
 int number = 10;
 
 int data[10] = {1,6,4,8,2,3,5,7,9,10};
 void quickSort(int *data, int start, int end){
 	if(start>=end){			// 원소가 1 개인 경우 
 		return;
	 }
	 int pivot = start;
	 int i = start + 1;
	 int j = end;
	 int temp;
	 while(i<=j){			// 엇갈릴 때까지 반복 
	 	while(data[i]>=data[pivot]){ // pivot값 보다 큰 값을 만날 때까지 반복 
	 		i++;
		 }
		 while(data[j]<=data[pivot] && j > start){// pivot 값 보다 작은 값을 만날 때까지 반복 
		 	j--;
		 }
		 if(i>j){			// 엇갈린 상태이면 
		 	temp = data[j];
		 	data[j] = data[pivot];
		 	data[pivot] = temp;
		} else{
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
		quickSort(data,start, j-1);
		quickSort(data,j+1, end);
	 } 
 }
 
 int main(){
 	int i;
 	quickSort(data, 0, number - 1);
 	for (i = 0; i < number ; i ++){
 		printf("%d ",data[i]);
	 }
	 return 0;
 }
