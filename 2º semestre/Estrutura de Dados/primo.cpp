#include <iostream>

using namespace std;

bool primo(int n) {
    for (int i = 2; i < n; i++){
        if(n % i == 0) {
            return false;
        }
    }

    return true;    
}

int main() {

    int a, b;

    do {
        cout << "Digite o número A:\n";
        cin >> a;

        cout << "Digite o número B:\n";
        cin >> b;
    } while(a > b);

    for(int i = a; i <= b; i++) {
        if(primo(i)) {
            cout << i << "\n";
        }
    }
    
    return 0;
}