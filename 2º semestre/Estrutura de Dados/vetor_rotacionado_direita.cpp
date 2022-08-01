#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int tamanhoVetor, qtdRotacionar;

    cin >> tamanhoVetor;
    cin >> qtdRotacionar;

    vector<int> numeros;
    numeros.reserve(tamanhoVetor);

    int numero;

    for(int i = 0; i < tamanhoVetor; i++) {
        cin >> numero;
        numeros.push_back(numero);
    }

    rotate(numeros.begin(),numeros.begin() + numeros.size() - qtdRotacionar,numeros.end());

    cout << "[ ";
    for(int i = 0; i < tamanhoVetor; i++) {
        cout << numeros[i] << " ";
    }

    cout << "]";
    cout << "\n";

    return 0;
}