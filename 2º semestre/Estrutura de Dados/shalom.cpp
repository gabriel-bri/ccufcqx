#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int size = 0, rotacoes = 0;
    cin >> size >> rotacoes;

    vector<int> vet(size);

    for(int i = 0; i < size; i++) {
        cin >> vet[i];
    }

    rotate(vet.begin(), vet.begin() + (size - rotacoes) % size, vet.end());

    cout << "[ ";
    for(int i = 0; i < size; i++) {
        cout << vet[i] << " ";
    }

    cout << "]\n";

    return 0;
}