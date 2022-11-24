package exercicios;

public class Exercicio5 {
	public static void main(String[] argvs){
		
		for(long i = 1; i <= 40; i++) {
			long resultado = 1;
			
			for(long j = 1; j <= i; j++) {
				resultado *= j;
			}
			
			System.out.println("O fatorial de " + i + " é igual a " + resultado);
		}

	}
	
	//Resposta: Pois os números começam a ficar muito grandes, logo não cabem dentro
	//do int sendo necessário utilizar o long para armazenas números maiores.
}
