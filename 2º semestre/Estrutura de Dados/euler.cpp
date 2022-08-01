#include <iostream>
#include <iomanip>

using namespace std;

int fat(int n) {
    if(n == 1) {
        return 1;
    }

    else {
        return n * fat(n - 1);
    }
}

float euler(float n) {
   float sum = 1;

    for(int i = 1; i <= n; i++) {
        sum += 1.0 / fat(i);
    }

   return sum;
    
}

double eulerR(int n) {
    if(n == 0) {
        return 1;
    }

    else {
        return 1.0 / fat(n) + eulerR(n - 1);
    }
}
int main() {
    int n;
    cout << "Digite um número para saber seu euler: ";    
    cin >> n;

    cout << "O euler de " << n << " é igual a " << ": " << euler(n) << "\n";

    cout << "O euler recurviso de " << n << " é igual a " << ": " << eulerR(n);
    return 0;
}