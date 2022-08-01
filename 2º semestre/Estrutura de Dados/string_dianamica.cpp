#include <iostream>

using namespace std;

int main() {
    int lim = 10;
    char* s = new char[10];
    char aux = ' ';
    char* novo;

    for(int i = 0; aux != '\n'; i++) {
        aux = std::getchar();

        if(i <= lim) {
            s[i] = aux;
        }

        else {
            lim += 10;

            novo = new char[i + 10];
            
            for(int j = 0; j < i; j++) {
                novo[j] = s[j];
            }

            novo[i] = aux;
            delete[] s;
            s = novo;
            novo = nullptr;
        }

    }

    for(int i = 0; s[i]; i++) {
        cout << s[i];
    }
    cout << "\n";

    delete[] s;
}