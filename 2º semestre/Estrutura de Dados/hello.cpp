#include <iostream>
#include <locale.h>

int main() {
    setlocale(LC_ALL,"portuguese"); 

    std::cout << "Olá mundo!\n";

    return 0;
}