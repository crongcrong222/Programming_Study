#include <iostream>
int factorial(int a){
    if (a > 1 ){
        return (a * factorial(a-1));
    }
    else{
        return 1;
    }
}

int main(void){
    int input;
    std:: cin >> input;
    std::cout << factorial(input) << std::endl;
    return 0;
}