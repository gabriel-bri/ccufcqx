#include <iostream>
#include <list>

using namespace std;

list<int> impares(int vet[], int size) {
    if(size == 0) {
        return list<int>();
    }

    if(vet[0] % 2 == 0) {
        return impares(vet + 1, size - 1);
    }

    auto lista = impares(vet + 1, size - 1);
    lista.push_front(vet[0]);
    return lista;
}

int main(){

    int vet[] = {3, 2, 1, 5, 6, 7, 2, 9};
    int size = sizeof(vet) / sizeof(int);

    for(auto value : impares(vet, size)){
        cout << value << " ";
    }

    cout << endl;
    return 0;
}