package componentes;
import java.util.Scanner;

class Main {
  public static void main(String[] args) { 
   
    Scanner sc = new Scanner(System.in);
    boolean end = false;

    while(!end){
      System.out.println("Digite um comando:");
      String line = sc.nextLine();
      String[] cmd = line.split(" ");
      String comando = cmd[0];
     
      switch(comando){
        case "addProf":
				if(cmd.length == 3) {
					
				}
				
				else {
					System.out.println("Ops, comando inválido");
				}
        	break;
        case "addSta":
        	if(cmd.length == 3) {
        		
        	}
        	
			else {
				System.out.println("Ops, comando inválido");
			}
        	
        	break;
        case "addTer":
        	if(cmd.length == 4) {
				
			}
			
			else {
				System.out.println("Ops, comando inválido");
			}
        	
        	break;
        	
        case "show":
        	if(cmd.length == 1) {
        		
        	}
        	
			else {
				System.out.println("Ops, comando inválido");
			}
        	break;
        	
        case "rm":
        	if(cmd.length == 2) {
        		
        	}
			
        	else {
				System.out.println("Ops, comando inválido");
			}
        	break;
        	
      }
    }
  }
}