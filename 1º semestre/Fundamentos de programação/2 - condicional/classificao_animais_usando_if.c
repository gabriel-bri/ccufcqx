#include <stdio.h>
#include <ctype.h>
int main()
{
    int classe, habitat, habito_alimentar;

    scanf("%d %d %d", &classe, &habitat, &habito_alimentar);
    
    // terrestre - mamifero
    if(classe == 1 &&  habitat == 1 && habito_alimentar == 1) {
        printf("Leão");
    }
    
    else if(classe == 1 && habitat == 1 && habito_alimentar == 2) {
        printf("Macaco");
    }
    
    else if(classe == 1 && habitat == 1 && habito_alimentar == 3) {
        printf("Cavalo");
    }
    
    // aquatico - mamifero
    
    else if(classe == 1 && habitat == 2 && habito_alimentar == 1) {
        printf("Foca");
    }
    
    else if(classe == 1 && habitat == 2 && habito_alimentar == 3) {
        printf("Peixe-boi");
    }
    
    // areo - mamifero
    
    else if(classe == 1 && habitat == 3 && (habito_alimentar == 1 || habito_alimentar == 2 || habito_alimentar == 3)) {
        printf("Morcego");
    }
    
    // ave - terrestre
    else if (classe == 2 && habitat == 1 && habito_alimentar == 4) {
        printf("Avestruz");
    }
    
    else if (classe == 2 && habitat == 1 && habito_alimentar == 2) {
        printf("Pinguim");
    }
    
    // ave - aquatico

    else if (classe == 2 && habitat == 2 && (habito_alimentar == 1 || habito_alimentar == 2)) {
        printf("Pato");
    }
    
    // ave - aereo
    
    else if (classe == 2 && habitat == 3 && (habito_alimentar == 1 || habito_alimentar == 2)) {
        printf("Águia");
    }
    return 0;
}
