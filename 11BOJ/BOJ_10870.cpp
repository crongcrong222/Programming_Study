#include <iostream>
int Fibonacci(int a){
    if (a > 1 ){
        return (Fibonacci(a-1) + Fibonacci(a-2));
    }
    else{
        return a;
    }
}

int main(void){
    int input;
    std:: cin >> input;
    std::cout << Fibonacci(input) << std::endl;
    return 0;
}