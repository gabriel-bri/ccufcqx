package exercicios;

public class Exercicio4 {
	
	public static void main(String[] argvs){
		
		for(int i = 1; i <= 10; i++) {
			int resultado = 1;
			
			for(int j = 1; j <= i; j++) {
				resultado *= j;
			}
			
			System.out.println("O fatorial de " + i + " é igual a " + resultado);
		}

	}
}
