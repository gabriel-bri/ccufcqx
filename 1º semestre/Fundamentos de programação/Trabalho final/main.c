#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
#include <locale.h>

typedef struct professor{
    int matricula;
    char nome[50];
    // mestrado, doutorado, graduação
    char maior_titulacao[50];
    //engenharia de software, rede de computadores.
    char area_pesquisa[50];
}Prof;

typedef struct disciplina{
    int num_disc;
    char nome_disc[50];
    int semestre;
    int creditos;
}Disciplina;

typedef struct associado{
    int mat_prof;
    int num_disc;
}Associado;


void inserir_professores(){
    FILE *p = fopen("professor.txt", "ab");
    int opc;
    Prof profe;
    do{
        printf("Digite a matricula, nome, maior titulação e area de pesquisa do professor\n");
        scanf(" %d", &profe.matricula);
        scanf(" %[^\n]", profe.nome);
        scanf(" %[^\n]", profe.maior_titulacao);
        scanf(" %[^\n]", profe.area_pesquisa);

        fwrite(&profe, sizeof(Prof), 1, p);

        printf("Deseja adicionar outro?\n 1- sim \n 0- nao");
        scanf("%d", &opc);
    }while(opc != 0);

    fclose(p);
}
void remover_professores(){
    FILE *pr = fopen("professor.txt","rb");
    FILE *p_m = fopen("associacao.txt","rb");
    int opc;
    int cont=0;
    int mat;
    Associado associado;
    Associado *assoc = malloc(sizeof(Associado));
    Prof profe;
    Prof *profs = (Prof *) malloc(sizeof(Prof));
    
    printf("Digite a matricula do professor que deseja remover.\n");
    scanf(" %d", &mat);

        
    while(fread(&profe,sizeof(Prof), 1, pr)){
        if(profe.matricula != mat){
            *(profs+cont) = profe;
            cont++;
            profs = (Prof *) realloc(profs, (cont+1)*sizeof(Prof));
        }   
    }
    fclose(pr);

    FILE *pw = fopen("professor.txt", "wb");
    for(int i=0; i<cont; i++){
       fwrite(profs+i, sizeof(Prof), 1, pw); 
    }
    fclose(pw);

    cont = 0;
    while(fread(&associado,sizeof(Associado), 1, p_m)){
        if(associado.mat_prof!=mat){
            *(assoc+cont) = associado;
            cont++;
            assoc = (Associado *) realloc(assoc, (cont+1)*sizeof(Associado));
        }
    }
    fclose(p_m);

    FILE *p_mw = fopen("associacao.txt", "wb");
    for(int i=0; i<cont; i++){
       fwrite(assoc+i, sizeof(Associado), 1, p_mw); 
    }
    fclose(p_mw);

    
}
void inserir_disciplinas(){
    FILE *d = fopen("disciplina.txt", "ab");
    Disciplina disc; 
    
        printf("Digite o numero, nome, semestre e creditos da disciplina\n");
        scanf(" %d", &disc.num_disc);
        scanf(" %[^\n]", disc.nome_disc);
        scanf(" %d", &disc.semestre);
        scanf(" %d", &disc.creditos);
        
    fwrite(&disc, sizeof(Disciplina), 1, d);

    fclose(d);
}
void remover_disciplinas(){
    FILE *d = fopen("disciplina.txt", "rb");
    FILE *p_m = fopen("associacao.txt", "rb");
    int cont = 0;
    int n;

    Associado associado;
    Associado *assoc = malloc(sizeof(Associado));
    Disciplina disc;
    Disciplina *disciplinas =  malloc(sizeof(Disciplina));

    printf("Digite o numero da disciplina a ser removida.");
    scanf(" %d", &n);

    while(fread(&disc,sizeof(Disciplina), 1, d)){
        if(disc.num_disc != n){
            *(disciplinas+cont) = disc;
            cont++;
            disciplinas = (Disciplina *) realloc(disciplinas, (cont+1)*sizeof(Disciplina));
        }
    }
    fclose(d);

    FILE *dw = fopen("disciplina.txt", "wb");
    for(int i=0; i<cont; i++){
       fwrite(disciplinas+i, sizeof(Disciplina), 1, dw); 
    }
    fclose(dw);

    cont = 0;
    while(fread(&associado,sizeof(Associado), 1, p_m)){
        if(associado.num_disc!=n){
            *(assoc+cont) = associado;
            cont++;
            assoc = (Associado *) realloc(assoc, (cont+1)*sizeof(Associado));
        }
    }
    fclose(p_m);

    FILE *p_mw = fopen("associacao.txt", "wb");
    for(int i=0; i<cont; i++){
       fwrite(assoc+i, sizeof(Associado), 1, dw); 
    }
    fclose(p_mw);
}
void associar_diciplinas(){
    
    //criacao do arquivo de associacao do prof e da disc.
    FILE *p_m = fopen("associacao.txt", "ab");
    //estrutura que contém todos os dados de professor e disciplina reunidos.
    Associado associado;
    Prof profe;
    Disciplina disc;
    
    int cont1=0;
    int cont2=0;
    
    while(cont1==0 || cont2==0){
        FILE *p = fopen("professor.txt", "rb");
        FILE *d = fopen("disciplina.txt", "rb");

        cont1=0;
        cont2=0;

        printf("\nDigite a matricula do professor e o numero da disciplina que quer associar.\n");
        scanf(" %d %d", &associado.mat_prof, &associado.num_disc);

        while(fread(&profe, sizeof(Prof), 1, p)){
            if(associado.mat_prof==profe.matricula) cont1++;
        }
        if(cont1==0){
            printf("Professor nao encontrado!\n");
        } 
        while(fread(&disc, sizeof(Disciplina), 1, d)){
            if(associado.num_disc==disc.num_disc) cont2++;
        }
        if(cont2==0){
            printf("Disciplina nao encontrada!");
        } 
        fclose(p);
        fclose(d);
    }
         

    fwrite(&associado, sizeof(Associado), 1, p_m);
    
    fclose(p_m);
    

}

int tamanho_arq(const char* nome_arq){
    FILE *f = fopen(nome_arq, "rb");

    if(f == NULL)
        return 0;

    fseek(f, 0, SEEK_END);
    int tam = ftell(f);
    fclose(f);

    return tam;
}

void imprimir_associacoes(){
    FILE *p_m = fopen("associacao.txt", "rb");
    

    Associado associado;
    Prof profe;
    Disciplina disc;
    
    if(tamanho_arq("associacao.txt") == 0) 
        printf("O arquivo esta vazio.");
    else{
        printf("----------------------------------------------\n");
        printf("Associacoes de professores\n");
        printf("----------------------------------------------\n");
        printf("Professor               Disciplina\n");
        while(fread(&associado, sizeof(Associado), 1, p_m) == 1){
            FILE *p = fopen("professor.txt", "rb");
            FILE *d = fopen("disciplina.txt", "rb");

            printf("%d - ", associado.mat_prof);
            while(fread(&profe, sizeof(Prof), 1, p) == 1){

                if(associado.mat_prof==profe.matricula){
                    printf("%s", profe.nome);
                }
            }
            printf("               ");
            printf("%d -", associado.num_disc);
            while(fread(&disc, sizeof(Disciplina), 1, d) == 1){
                if(associado.num_disc==disc.num_disc){
                    printf("%s\n", disc.nome_disc);
                }
            }
        fclose(p);
        fclose(d);            
        }
    }
    fclose(p_m);
}

void imprimir_professores(){
    FILE *p = fopen("professor.txt", "rb");

    Prof profe;
    if(tamanho_arq("professor.txt") == 0) 
        printf("O arquivo esta vazio.");
    else{
        printf("----------------------------------------------\n");
        printf("Registro de professores\n");
        printf("----------------------------------------------\n");
        printf("Professor     Matricula\n");
        while(fread(&profe, sizeof(Prof), 1, p) == 1){
            printf("%s -", profe.nome);
            printf("     %d \n", profe.matricula);
        }
    }
    fclose(p);
}

void imprimir_disciplinas(){
    FILE *d = fopen("disciplina.txt", "rb");
    Disciplina disc;

    if(tamanho_arq("disciplina.txt") == 0) 
        printf("O arquivo esta vazio.");
    else{
        printf("----------------------------------------------\n");
        printf("Registro de disciplinas\n");
        printf("----------------------------------------------\n");
        while(fread(&disc, sizeof(Disciplina), 1, d) == 1){
            printf("nome: %s -", disc.nome_disc);
            printf("numero: %d \n", disc.num_disc);
        }
    }
   
    fclose(d);
}

int main(){
    setlocale(LC_ALL,"Portuguese");
    int opc;
    do{
        printf("Selecione a opcao desejada:\n1- Inserir professor\n 2-Remover professor\n 3- Inserir disciplina\n 4- Remover disciplina\n 5-Associar professor a disciplina \n 6- Imprimir associacao \n 7- imprimir professor \n 8-imprimir disciplina \n 9- sair\n");
        scanf("%d", &opc);
        
        switch(opc){
            case 1:
                inserir_professores();
                break;
            case 2:
                remover_professores();
                break;
            case 3:
                inserir_disciplinas();
                break;
            case 4:
                remover_disciplinas();
                break;
            case 5:
                associar_diciplinas();
                break;
            case 6:
                imprimir_associacoes();
                break;
            case 7:
                imprimir_professores();
                break;
            case 8:
                imprimir_disciplinas();
                break;
            case 9:
                printf("Encerrando");
                break;
            default:
                printf("Opcao invalida!");
        }
        
    }while(opc!=9);
      
    return(0);
}
