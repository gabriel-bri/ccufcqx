package exercicios;

public class Exercicio5 {
	public static void main(String[] argvs){
		
		for(long i = 1; i <= 40; i++) {
			long resultado = 1;
			
			for(long j = 1; j <= i; j++) {
				resultado *= j;
			}
			
			System.out.println("O fatorial de " + i + " � igual a " + resultado);
		}

	}
	
	//Resposta: Pois os n�meros come�am a ficar muito grandes, logo n�o cabem dentro
	//do int sendo necess�rio utilizar o long para armazenas n�meros maiores.
}
