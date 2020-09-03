#include <stdio.h>

int main(){
	int profundidade= 0;
	int salto = 0;
	int escorrega = 0;
	int profundidadeAtual = 0;

	printf("Digite a profundidade do poço:");
	scanf("%d", &profundidade);

	printf("Digite o salto: ");
	scanf("%d", &salto);
	
	printf("Digite o escorregamento: ");
	scanf("%d", &escorrega);

	while(profundidadeAtual < profundidade) {
		printf("%d", profundidadeAtual);
		profundidadeAtual += salto;

		if(profundidadeAtual < profundidade) {
			printf(" %d\n", profundidadeAtual);
			profundidadeAtual -= escorrega;
			salto - 10; 
		}
	}

	printf("saiu\n"); 
    return 0;
}
