#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Pessoa {
    string nome;
    int idade;
};

bool menor_que(Pessoa a, Pessoa b) {
    return (a.idade < b.idade) ? true : false;
}


template< typename T >
void bubblesort(T b, T e) {
    T penultimo = b;
    while(penultimo+1 != e)
        penultimo++;
    
    for(T i = penultimo; i != b; --i)
        for(T j = b; j != i; ++j)
            if(*j > *(j+1)) 
            {
                auto aux = *j;
                *j = *(j+1);
                *(j+1) = aux;
            }

}

template< typename T, typename F>
void bubblesort(T b, T e, F func) {
    T penultimo = b;
    while(penultimo+1 != e)
        penultimo++;
    
    for(T i = penultimo; i != b; --i)
        for(T j = b; j != i; ++j)
            if(!func(*j, *(j+1)))
            {
                auto aux = *j;
                *j = *(j+1);
                *(j+1) = aux;
            }

}


int main() {

    vector<Pessoa> vec = { {"Atilio", 56}, {"Maria", 23}, {"Ana", 12}, {"Joao", 5} };

    bubblesort(vec.begin(), vec.end(), menor_que);

    for(auto e : vec)
        cout << e.nome << " " << e.idade << endl;
    
    cout << endl;
    

    vector<int> vint = {23, 45, 78, 1, 4, 9, 3};

    bubblesort(vint.begin(), vint.end());

    for(auto e : vint)
        cout << e << " ";
    
    cout << endl;

    return 0;
}