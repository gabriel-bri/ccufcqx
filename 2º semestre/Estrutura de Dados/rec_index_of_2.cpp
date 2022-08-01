#include <iostream>

using namespace std;

int index_of2(int vet[], int size, int value, int index = 0) {
    if(size == 0) {
        return -1;
    }

    if(vet[0] == value) {
        return index;   
    }

    return index_of2(vet + 1, size - 1, value, index + 1);
}

int main(){

    int vet[] = {3, 2, 1, 5, 6, 7, 2, 9};
    int size = sizeof(vet) / sizeof(int);

    cout << index_of2(vet, size, 6) << endl;

    return 0;
}