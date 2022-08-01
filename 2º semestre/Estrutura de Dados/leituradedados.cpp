#include <iostream>

using namespace std;
int main() {

    cout << "Digite seu nome:\n";
    string nome;
    cin >> nome;
    
    cout << "Digite sua idade:\n";
    int idade;
    cin >> idade;

    cout << "Olá, " << nome << "! Você tem " << idade << " anos!";

    return 0;
}