#include <iostream>

using namespace std;

void printReverse(int* v, int n) {
    if(n >= 0 ) {
        cout << "------------------------- \n";
        cout << "<< " << v[n] << " << \n";
        printReverse(v, n - 1);

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

    printReverse(v, n - 1);
    return 0;
}