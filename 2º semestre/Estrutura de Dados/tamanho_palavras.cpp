#include <iostream>

using namespace std;

int strcmp(char *str1, char *str2) {
    for(int i = 0; str1[i] != '\0' && str2[i] != '\0'; i++) {
        if(str1[i] > str2[i]) {
            return 1;
        }

        else if(str1[i] < str2[i]) {
            return -1;
        }
    }

    return 0;
}

int strlen(char* s) {
    int size = 0;
    for(int i = 0; s[i]; i++) {
        size++;
    }

    return size;
}

int main() {
    char s1[25], s2[25];
    cin >> s1;
    cin >> s2;

    cout << "String 1: " << s1 << "\n";
    cout << "String 2: " << s2 << "\n";

    cout << "O tamanho de String 1 é de: " << strlen(s1) << "\n";
    cout << "O tamanho de String 2 é de: " << strlen(s2) << "\n";

    cout << "O resultado da comparação é: " << strcmp(s1, s2) << "\n";     
    return 0;
}