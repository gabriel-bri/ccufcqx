#include <stdio.h>
#include <ctype.h>

int main(){
    char novos_casos_, mortes_, novos_casos, mortes;
    scanf("%c %c", &novos_casos_, &mortes_);
    
    novos_casos = toupper(novos_casos_);
    mortes = toupper(mortes_);
    
    switch(novos_casos) {
        case 'A':
            printf("Isolamento");
        break;
        
        case 'D':
            switch(mortes) {
                case 'A':
                    printf("Isolamento");
                break;
                
                case 'D':
                    printf("Fim do isolamento");
                break;
            }
        break;
    }
    return 0;
}
