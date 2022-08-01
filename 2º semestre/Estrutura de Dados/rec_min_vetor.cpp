#include <iostream>

using namespace std;

int vet_min(int vet[], int size) {
    if(size == 1) {
        return vet[0];
    }

    int eu = vet[0];
    int menor_do_resto = vet_min(vet + 1, size - 1);

    return min(eu, menor_do_resto);
}

int main(){

    int vet[] = {3, 2, 1, 5, 6, 7, 2, 9};
    int size = sizeof(vet) / sizeof(int);

    cout << vet_min(vet, size) << endl;

    return 0;
}