#include <iostream>

using namespace std;

int main() {

    int x = 10;
    int* y = &x;

    x += 1;
    
    cout << "X tem o valor de: " << x << "\n";
    cout << "y tem o valor de: " << y << "\n";
    cout << "*y tem o valor de: " << *y << "\n";

    return 0;
}