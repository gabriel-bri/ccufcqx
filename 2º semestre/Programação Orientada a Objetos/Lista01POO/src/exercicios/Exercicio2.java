package exercicios;

public class Exercicio2 {
	public static void main(String[] argvs) {
		int soma = 0;
		
		for(int i = 1; i <= 1000; i++) {
			soma += i;
		}
		
		System.out.println("A soma de 1 a 1000 é igual a " + soma);
	}
}
