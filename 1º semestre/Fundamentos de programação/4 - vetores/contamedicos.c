#include <stdio.h>

int main(){
    int tamanho = 4;
    
    printf("Digite quantos soldados a tropa terá: ");
    scanf("%d", &tamanho);
    
    int tropa[tamanho], semmedicos = 0;
    
    for(int i = 0; i < tamanho; i++) {
        printf("Digite a numeração do soldado %d: ", i);
        scanf("%d", &tropa[i]);
    }
    
    for(int i = 0; i < tamanho; i++) {
        if(tropa[i] == 0 && (tropa[i + 1] != 1 || tropa[i - 1] != 1)) {
            semmedicos++;
        }
        
    }
    
    printf("%d", semmedicos);
    return 0;
}
