#ifndef STACK_H
#define STACK_H
#include <ostream>
#include <string>
#include <vector>

template< typename T >
class Stack {
private:
    std::vector<T> pilha;

public:
    void push(T& item) {
        pilha.push_back(item);
    }

    void pop() {
        pilha.pop_back();
    }

    T& top() {
        return pilha.back();
    }

    int length() {
        return pilha.size();
    }

    bool empty() {
        return pilha.empty();
    }

    // Sobrecarregando o operador<<
    // Ao passar um objeto desta classe para o operador <<, os elementos da pilha serao
    // impressos do topo para a base da pilha
    friend std::ostream& operator<<(std::ostream& out, Stack& p) {
        std::string str = "Stack[";
        for(int i = p.length()-1; i >= 0; i--) {
            str += std::to_string(p.pilha[i]);
            if(i >= 1) str += ",";
        }
        str += "]";
        out << str;
        return out;
    } 
};

#endif
