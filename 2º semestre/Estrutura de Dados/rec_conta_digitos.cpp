#include <iostream>

using namespace std;

int conta_digitos(int value) {
    return value < 10 ? 1 : 1 + conta_digitos(value / 10);
}

int main() {
    int numero;
    cin >> numero;

    cout << "rec: " << conta_digitos(numero) << "\n";

    return 0;
}