package componentes;

public class Professor extends Funcionario{
	
	private char classe;
	private Funcionario f;
	
	Professor(String nome, char classe) {
		super(nome, 2);
		this.setNome(nome);
		this.setClasse(classe);
	}

	public double calcSalario() {
		double salario = 0;
		switch(this.getClasse()) {
			case 'A':
				salario = 3000;
			break;
			
			case 'B':
				salario = 5000;
			break;
				
			case 'C':
				salario = 7000;
			break;
			
			case 'D':
				salario = 9000;
			break;
			
			case 'E':
				salario = 1100;
			break;
 		}
		return salario;
	}
	public char getClasse() {
		return classe;
	}
	
	public void setClasse(char classe) {
		this.classe = classe;
	}
	
	
}
