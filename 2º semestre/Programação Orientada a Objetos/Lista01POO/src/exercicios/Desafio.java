package exercicios;

public class Desafio {
	public static void main(String[] args){
		
		int t1 = 0;
		int t2 = 1;
		
		while(t2 <= 100) {
			System.out.println(t2);
			
			t1 += t2;
			
			t2 += t1;
		}
		
	}
}
