#include <iostream>
#include "Stack.h"

using namespace std;

int main() {
    Stack<int> p;

    for(int i = 1; i <= 10; i++) {
        p.push(i);
        cout << "empilhou:" << p.top() << endl;
    }
    
    cout << p << endl; // Imprime a pilha na tela

    while(!p.empty()) {
        cout << "desempilhou: " << p.top() << endl;
        p.pop();
    }

    
    return 0;
}