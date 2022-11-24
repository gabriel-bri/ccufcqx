package exercicios;

public class Exercicio6 {
	public static void main(String[] argvs){
		long t1 = 0, t2 = 1, t3 = 0;
		
		for(long i = 1; t1 + t2 <= 100; i++) {
			t3  = t2 + t1; 
			t1  = t2;
		    t2 = t3;
		    
			System.out.println("A sequência é " + t2);
		}
	}
}
