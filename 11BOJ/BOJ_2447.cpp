#include <stdio.h>

 void Fractal(int i, int j, int number){
     if( (i/number)  % 3 == 1 && (j/number)  % 3 == 1){
         printf(" ");
     }
     else{
         if(number == 1){
             printf("*");
         }
         else{
             Fractal(i, j, number/3);
         }
     }
 }
 int main(){
     int number;
     scanf("%d",&number);
     for(int i = 0; i < number; i ++){
         for(int j = 0; j < number; j++){
             Fractal(i,j,number);
         }
         printf("\n");
     }
     return 0;
 }