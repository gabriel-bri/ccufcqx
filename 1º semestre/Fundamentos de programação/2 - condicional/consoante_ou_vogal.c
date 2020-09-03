#include <stdio.h>
#include <ctype.h>
int main()
{
    char letra, letra_maiuscula;
    
    scanf("%c \n", &letra);
    
    letra_maiuscula = toupper(letra);
    
    switch (letra_maiuscula) {
        case 'A':
            printf("VOGAL");
        break;
        
        case 'E':
            printf("VOGAL");
        break;
        
        case 'I':
            printf("VOGAL");
        break;

        case 'O':
            printf("VOGAL");
        break;

        case 'U':
            printf("VOGAL");
        break;
        
        default:
            printf("CONSOANTE");
    }
    
    return 0;
}
