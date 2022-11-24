package exercicios;

public class TestaSplit {
	public static void main(String[] argvs){
		String frase = "Socorram-me, subi no ônibus em Marrocos";
		
		String[] palavras = frase.split(" ");
		
		for(int i = 0; i < palavras.length; i++) {
			System.out.println(palavras[i]);
		}
	}
}
