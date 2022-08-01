#include <iostream>

using namespace std;

int fib(int n) {
    if ( n == 0 || n == 1) {
        return 1;
    }

    else {
        return fib(n - 1) + fib(n - 2);
    }
}

int main() {
    cout << "Digite um número para saber o fibonacci dele: ";
    int n;
    cin >> n;

    for(int i = 0; i <= n; i++) {
        cout << "fib(" << i << "): " << fib(i) << "\n";
    }
    return 0;
}