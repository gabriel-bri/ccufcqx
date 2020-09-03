
#include <stdio.h>

int main()
{
    int classe, habitat, habito_alimentar;
    
    scanf("%d %d %d", &classe, &habitat, &habito_alimentar);
    
    switch(classe) {
        case 1:
            if(habitat == 1 && habito_alimentar == 1) {
                printf("Leão");
            }
            
            else if(habitat == 1 && habito_alimentar == 2) {
                printf("Macaco");
            }
    
            else if(habitat == 1 && habito_alimentar == 3) {
                printf("Cavalo");
            }
            
            else if(habitat == 2 && habito_alimentar == 1) {
                printf("Foca");
            }
    
            else if(habitat == 2 && habito_alimentar == 3) {
                printf("Peixe-boi");
            }
    
            // areo - mamifero
    
            else if(habitat == 3 && (habito_alimentar == 1 || habito_alimentar == 2 || habito_alimentar == 3)) {
            printf("Morcego");
            }
        break;
        
        case 2:
            // ave - terrestre
            if (habitat == 1 && habito_alimentar == 4) {
                printf("Avestruz");
            }
            
            else if (habitat == 1 && habito_alimentar == 2) {
                printf("Pinguim");
            }
            
            // ave - aquatico
        
            else if (habitat == 2 && (habito_alimentar == 1 || habito_alimentar == 2)) {
                printf("Pato");
            }
            
            // ave - aereo
            
            else if (habitat == 3 && (habito_alimentar == 1 || habito_alimentar == 2)) {
                printf("Águia");
            }
        break;
    }
    return 0;
}
