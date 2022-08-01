#include <iostream>

using namespace std;

int** lerMatriz(int n) {
    int** m = new int*[n];

    for (int i = 0; i < n; i++) {
        m[i] = new int[n];
    }
    return m;
}

void setMatriz(int** m, int n) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> m[i][j];
        }        
    }
}

void printM(int** m, int n) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << m[i][j] << " ";
        }
        cout << "\n";        
    }
}

void destroiMatriz(int** m, int n) {
    for(int i = 0; i < n; i++) {
        delete[] m[i];        
    }

    delete[] m;
}

int sumLine(int* v, int n) {
    int soma = 0;
   
    for(int i  = 0; i <= n; i++) {
        soma += v[i];
    }

    return soma;
}

int sumCol(int** v, int n, int col) {
    int soma = 0;

    for(int i  = 0; i <= n; i++) {
        v[i][col];
    }

    return soma;
}

int sumDiagP(int** m, int n) {
    int soma = 0;

    for(int i  = 0; i <= n; i++) {
        soma += m[i][i];
    }

    return soma;
}

int sumDiagS(int** m, int n) {
    int soma = 0;

    for(int i  = 0; i <= n; i++) {
        soma += m[i][n - 1];
    }

    return soma;   
}

bool QuadradoMagico(int** m, int n) {
    int param = sumDiagP(m, n);
    int dS = sumDiagS(m, n);
    int lin, col;

    if(param != dS)
        return false;
    
    for(int i = 0; i < n; i++) {
        lin = sumLine(m[i], n);
        col = sumCol(m, n, i);

        if(lin != param && col != param) {
            return false;
        }

    }

    return true;
}
int main() {

    int** M = lerMatriz(3);
    setMatriz(M, 3);
    printM(M, 3);

    if(QuadradoMagico(M, 3)) {
        cout << "Sim, é quadrado.";
    }

    else {
        cout << "Não, não é quadrado.";
    }

    destroiMatriz(M, 3);
    return 0;
}