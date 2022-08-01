#include <iostream>

using namespace std;

int index_of(int vet[], int size, int value) {
    if(size == 0) {
        return -1;
    }

    if(vet[0] == value) {
        return 0;   
    }

    int dist = index_of(vet + 1, size - 1, value);

    if(dist == -1) {
        return -1;
    }

    return dist + 1;
}

int main(){

    int vet[] = {3, 2, 1, 5, 6, 7, 2, 9};
    int size = sizeof(vet) / sizeof(int);

    cout << index_of(vet, size, 6) << endl;

    return 0;
}