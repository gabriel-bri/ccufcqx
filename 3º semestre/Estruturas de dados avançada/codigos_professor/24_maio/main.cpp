#include <iostream>
#include <string>
#include <stdexcept>
#include <iomanip>
#include <vector>
#include "Codification.h"
#include "HashTable.h"
using namespace std;

int main() 
{
    // cria tabela hash
    HashTable<std::string, unsigned long int> ht (3, 2.0, 5.0, code_std_string);

    // adiciona pares de elementos
    ht["atilio"] = 1313131313;
    ht["julio"] = 12;
    ht["bia"] = 19;
    ht["mariliza"] = 21;
    ht["lia"] = 22;
    ht["carlos"] = 23;
    ht["dora"] = 24;
    ht["maria"] = 25;

    // imprime valores
    cout << ht["atilio"] << endl;
    cout << ht["julio"] << endl;
    cout << ht["bia"] << endl;
    cout << ht["mariliza"] << endl;
    cout << ht["lia"] << endl;
    cout << ht["carlos"] << endl;
    cout << ht["dora"] << endl;
    cout << ht["maria"] << endl;
    cout << ht["jurema"] << endl; // nao existe, mas sera incluida automaticamente 

    // remove alguns
    ht.remove("atilio");

    // tenta imprimir na tela o valor do par que foi removido,
    // mas vai lancar excecao
    try {
        cout << ht.at("atilio") << endl;
    }
    catch(const exception& e) {
        cout << "erro: " << e.what() << endl;
    }

}
