#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
typedef struct cliente{
    int numero;
    char nome[20];
}Cliente;

void inserir(){
    FILE *f = fopen("clientes.txt", "ab+");
    
    Cliente c;
    printf("Digite ndo cliente");
    scanf("%d", &c.numero);
    scanf("%s", c.nome);
    
    fwrite(&c, sizeof(Cliente), 1, f);
    
    fclose(f);
}

void imprimir(){
    setlocale(LC_ALL, "Portuguese");
    FILE *f = fopen("clientes.txt", "rb");
    
    Cliente c;
    while(fread(&c,sizeof(Cliente), 1, f)){
        printf("N= %d", c.numero);
        printf("Nome do cliente = %s\n", c.nome);
    }   
    
    fclose(f);
}


void imprimir_cliente_especifico(){
    FILE *f = fopen("clientes.txt", "rb");
    int num;
    
    printf("Digite o n do cliente que vos dados");
    scanf("%d", &num);
    int temp =0;
    
    Cliente c;
    while(fread(&c,sizeof(Cliente), 1, f)){
        if(c.numero == num){
            printf("N do cliente = %d", c.numero);
            printf("Nome do cliente = %s\n", c.nome);
            temp =0;
        }
        
    }
    
    if(temp == 0) printf("Cliente no encontrado");
    
    fclose(f);
}

void remover(){
    FILE *f = fopen("clientes.txt", "rb");
    int cont=0;
    int num;
    
    Cliente c;
    Cliente *clientes = (Cliente*) malloc(sizeof(Cliente));
    
    printf("Digite o n do cliente a ser removido");
    scanf("%d", &num);
    
    while(fread(&c,sizeof(Cliente), 1, f)){
        if(c.numero != num){
            *(clientes+cont) = c;
            cont++;
            clientes = (Cliente*) realloc(clientes, (cont+1)* sizeof(Cliente));
        }
    }
    
    fclose(f);
    
    FILE *fw = fopen("clientes.txt", "wb");
    int i;
    for( i=0; i<cont;i++)
        fwrite(clientes+i, sizeof(Cliente), 1, fw);
    
    fclose(fw);
}

int main(){
    int opc;
    
    do{
        printf("Selecione a op desejada: 1- inserir, 2-remover, 3- imprimir, 4- encerrar");
        scanf("%d", &opc);
        
        switch(opc){
            case 1:
                inserir();
                break;
            case 2:
                remover();
                break;
            case 3:
                imprimir();
                break;
            case 4:
                printf("Encerrando");
                break;
            default:
                printf("no");
        }
        
    }while(opc!=4);
      
    return(0);
}
