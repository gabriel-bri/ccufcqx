#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int qtdPessoas, totalRemover, quemRemover;

    cin >> qtdPessoas;

    vector <int> pessoas;
    pessoas.reserve(qtdPessoas);

    for(int i = 0; i < qtdPessoas; i++) {
        cin >> pessoas[i];
    }

    cin >> totalRemover;



    for(int j = 0; j < pessoas.size(); j++) {
        cout << "Dados " << pessoas[j] << "\n";
        for(int i = 0; i < totalRemover; i++) {
            cin >> quemRemover;
            cout << "Procurando por " << quemRemover << "\n";
            if(pessoas[i] == quemRemover) {
                pessoas.erase(pessoas.begin() + j);                
            }   
        }

    }

    for(int valor : pessoas) 
        cout << valor << " ";
    return 0;
}