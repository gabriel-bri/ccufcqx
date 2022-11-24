package view;

import java.util.Scanner;
import control.RepositorioPessoa;
import model.Pessoa;

public class Main {
	public static void main(String[] args) {
		Pessoa p = null;
		RepositorioPessoa rp = new RepositorioPessoa();
		String cmd;
		Scanner s = new Scanner(System.in);
		
		boolean continuar = true;
		System.out.println("Comandos: \n" + "addpessoa nome idade\n" + "buscar nome\n" + "comandos\n" + "show\n" + "sair");
		
		while(continuar != false) {
			cmd = s.next();
			String[] comando = cmd.split(" ");
			
			switch(comando[0]) {
				case "addpessoa":
					try {
						p = new Pessoa(comando[1], Integer.parseInt(comando[2]));
						rp.add(p);
					}
					
					catch(Exception e) {
						System.out.println(e.getMessage());
					}
					
					finally {
						rp.toString();
					}
					
				break;
				
				case "buscar":
					try {
						rp.buscar2(comando[1]);
					}
					
					catch(Exception e) {
						System.out.println(e.getMessage());
					}
					
					finally {
						rp.toString();
					}
				break;
				
				case "show":
					rp.toString();
				break;
				
				case "comandos":
					System.out.println("Comandos: \n" + "addpessoa nome idade\n" + "buscar nome\n" + "comandos\n" + "show\n" + "sair");
				break;
				case "sair":
					System.out.println("Saindo da aplicação...");
					System.exit(0);
					continuar = false;
				break;
				
				default:
					System.out.println("Comando inválido, tente de novo.");
			}
		}
	}
}
