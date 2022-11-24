package pet;

import java.util.Scanner;

public class TestePet {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Pet tamagoshi = new Pet(3, 3, 3);
		
		System.out.println("========================================");
		System.out.println("Bem vindo ao ambiente do seu pet virtual");
		System.out.println("========================================");
		
		int op = 0;
		
		do {
			System.out.println("========================================");
			System.out.println("[0] para sair\n"
					+ "[1] para brincar\n"
					+ "[2] para banhar\n"
					+ "[3] para comer\n"
					+ "[4] para dormir\n"
					+ "[5] para mostrar as informa��es\n");
			System.out.println("========================================");
			System.out.println("Digite uma op��o: ");
			op = input.nextInt();
			
			switch(op) {
				case 0:
					System.out.println("Fechando o jogo :(");
					break;
				
				case 1:
					tamagoshi.play();
					break;
				
				case 2:
					tamagoshi.shower();
					break;
				
				case 3:
					tamagoshi.eat();
					break;
				
				case 4:
					tamagoshi.sleep();
					break;
					
				case 5:
					tamagoshi.show();
					break;
				
				default:
					System.out.println("Op��o inv�lida :/");
			}
 		}while(op != 0);
	}
}
