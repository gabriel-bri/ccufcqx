#include <iostream>

using namespace std;

int fat(int n) {
    if(n == 1) {
        return 1;
    }

    else {
        return n * fat(n - 1);
    }
}

int main() {
    int n;
    cout << "Digite um número para saber seu fatorial: ";    
    cin >> n;

    cout << "O fatorial de " << n << " é igual a " << ": " << fat(n);
    return 0;
}