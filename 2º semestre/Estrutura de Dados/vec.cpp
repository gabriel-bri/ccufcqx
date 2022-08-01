#include <iostream>

using namespace std;

int somaR(int* v, int n) {
    if(n == 0) {
        return 0;
    }

    else {
        return v[n - 1] + somaR(v, n - 1);
    }   
}

int main() {
    int n;
    
    cout << "Digite o tamanho do vetor: \n"; 
    cin >> n;

    int v[n];

    for(int i = 0; i < n; i++) {
        cin >> v[i];
       }

    cout << "A soma dos valores do vetor é igual a: " << somaR(v, n);
    return 0;
}