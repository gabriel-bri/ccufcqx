#include <iostream>

using namespace std;

void mm(int A[], int n, int *min, int *max) {
    for(int i = 0; i < n; i++) {
        if(i == 0) {
            *min = A[i];
            *max = A[i];
        }

        if(A[i] > *max) {
            *max = A[i];
        }

        if(A[i] < *min) {
            *min = A[i];
        }
    }
}

int main() {
    int n;
    cout << "Digite o tamanho do vetor: \n";

    cin >> n;
    int v[n];
    int maior, menor;

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    mm(v, n, &menor, &maior );

    cout << "Menor: " << menor << "\n";
    cout << "Maior: " << maior << "\n";
    return 0;
}