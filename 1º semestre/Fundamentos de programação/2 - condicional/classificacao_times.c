#include <stdio.h>

int main(){
    int serie_a, sede, uniforme;
    
    scanf("%d %d %d", &serie_a, &sede, &uniforme);
    
    switch(serie_a) {
        // quem tá na série a
        case 1:
            switch(sede) { // sede
                case 1: //times da sede
                    switch(uniforme) {
                        case 1:
                            printf("Ceará");
                        break;
                        
                        case 2:
                            printf("Não tem");
                        break;
                    }
                break;
                
                case 2:
                    printf("Sem times do interior na série A");
                break;
            }
        break;
        
        case 2:
            switch(sede) {
                case 1:
                    switch(uniforme) {
                      case 1:
                        printf("Não tem");
                      break;
                      
                      case 2:
                        printf("Fortaleza e Floresta");
                      break;
                    }
                break;
                
                case 2:
                    switch(uniforme) {
                        case 1:
                            printf("Não tem");
                        break;
                        
                        case 2:
                            printf("Guarany");
                        break;
                    }
                break;
            }
        break;
    }
    return 0;
}
