#include <iostream>
#include <list>

using namespace std;

list<int> impares2(int vet[], int size, list<int> &acc) {
    if(size == 0) {
        return acc;
    }

    if(vet[0] % 2 == 0) {
        return impares2(vet + 1, size - 1, acc);
    }
    acc.push_back(vet[0]);
    return impares2(vet + 1, size - 1, acc);
}

int main(){

    int vet[] = {3, 2, 1, 5, 6, 7, 2, 9};
    int size = sizeof(vet) / sizeof(int);

    list<int> lista;
    for(auto value : impares2(vet, size, lista)){
        cout << value << " ";
    }

    cout << endl;
    return 0;
}