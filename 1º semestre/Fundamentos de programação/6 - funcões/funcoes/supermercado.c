#include <stdio.h>
int p[4];

void adicionar() {
    int quantidade, id;
    
    printf("Digite o código do produto e sua quantidade para ser adicionada:\n");
    printf("0- Arroz, 1- Feijão, 2- Biscoito, 3-Molho de tomate\n");
    scanf("%d", &id);
    scanf("%d", &quantidade);
    
    switch(id) {
        case 0:
            p[0] += quantidade;
            printf("Produto adicionado com sucessozn\n");
        break;
        
        case 1:
            p[1] += quantidade;
            printf("Produto adicionado com sucessozn\n");
        break;
        
        case 2:
            p[2] += quantidade;
            printf("Produto adicionado com sucessozn\n");
        break;
        
        case 3:
            p[3] += quantidade;
            printf("Produto adicionado com sucesso!\n");
        break;
        
        default:
            printf("Produto inválido\n");
            adicionar();
    }
}

void remover() {
    int quantidade, id;
    
    printf("Digite o código do produto e sua quantidade a ser removida:\n");
    printf("0- Arroz, 1- Feijão, 2- Biscoito, 3-Molho de tomate\n");
    scanf("%d", &id);
    scanf("%d", &quantidade);
    
    switch(id) {
        case 0:
            if(quantidade <= p[0]) {
                p[0] -= quantidade;
                printf("Produto removido com sucessozn\n");              
            }
        break;
        
        case 1:
            if(quantidade <= p[1]) {
                p[1] -= quantidade;
                printf("Produto removido com sucessozn\n");              
            }
        break;
        
        case 2:
            if(quantidade <= p[2]) {
                p[2] -= quantidade;
                printf("Produto removido com sucessozn\n");              
            }
        break;
        
        case 3:
            if(quantidade <= p[3]) {
                p[3] -= quantidade;
                printf("Produto removido com sucessozn\n");              
            }
        break;
        
        default:
            printf("Produto inválido\n");
            remover();
    }
}

int main(){
    int opc;
    
    do {
        printf("Digite uma opção:\n");
        printf("1 - Adicionar produtos \n2 - Remover produtos \n3 - Encerrar\n");
        scanf("%d", &opc);
        
        switch(opc) {
            case 1:
                adicionar();
            break;
            
            case 2:
                remover();
            break;
            
            case 3:
                printf("Encerrando o programa...");
            break;
            
            default:
                printf("Opção inválida, tente novamente!\n");
        }
        
    } while(opc != 3);
    
    printf("Quantidade de produtos no estoque:\n");
    printf("%d - Arroz, %d - Feijão, %d - Biscoito, %d - Molho de tomate\n", p[0], p[1], p[2], p[3]);
    return 0;
}
