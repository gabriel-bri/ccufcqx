#include <iostream>
#include <locale.h>

using namespace std;

void printV(int v[], int n) {
    for (int i = 0; i < n; i++){
        cout << "Posição " << i << " tem o valor de: " << v[i] << "\n";
    }
    

}
int main() {

    int tam;

    cout << "Qual o tamanho do vetor que você deseja?\n";
    cin >> tam;
    
    int vet_int[tam];

    for(int i = 0; i < tam; i++) {
        cout << "Digite o valor da posição " << i <<":\n";
        cin >> vet_int[i];
    }
    printV(vet_int, tam);

    return 0;
}