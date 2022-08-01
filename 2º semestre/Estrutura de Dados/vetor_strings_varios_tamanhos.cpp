#include <iostream>
#include <cstdlib>

using namespace std;

int strcmp(char* a, char* b) {
    for(int i = 0; a[i] || b[i]; i++) {
        if(a[i] < b[i]) {
            return -1;  
        }

        else if(a[i] > b[i]) {
            return 1;
        }
    }

    return 0;
}

void ordena(char** v, int n) {
    for(int i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - 1; j++) {
            if( strcmp(v[j], v[j + 1]) == 1) {
                char* aux = v[j];

                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
        }
    }
}

void strPrint(char* s) {
    for(int i = 0; s[i]; i++) {
        cout << s[i];
    }

    cout << "\n";
}

int main() {

    int n;
    cin >> n;

    char ** v = new char*[n];

    int l;

    for(int i = 0; i < n; i++) {
        cin >> l;
        v[i] = new char[l];
        cin.ignore();
        cin.get(v[i], l + 2);

    }

    ordena(v, n);

    cout << "=============================\n";
    for(int i = 0; i < n; i++) {
        strPrint(v[i]);
    }

    for(int i = 0; i < n; i++) {
        delete[] v[i];
    }

    delete[] v;

    return 0;
}