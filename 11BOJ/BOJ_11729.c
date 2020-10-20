#include <stdio.h>
#include <math.h>

void hanoi(int num, int from, int mid, int to){
    if(num == 1){
        printf("%d %d\n",from, to);
    }
    else{
        hanoi(num-1, from, to, mid);
        printf("%d %d\n",from, to);
        hanoi(num-1, mid, from, to);
    }
}

int main(){
    int n;
    int count;
    scanf("%d",&n);
    count = pow(2, n) - 1;
    printf("%d\n",count);
    hanoi(n,1,2,3);
    return 0;
}