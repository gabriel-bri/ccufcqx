package componentes;

public class Funcionario {
	protected String nome;
	protected int max_diarias;
	protected int qtd_diarias;
	protected double bonus;
	
	Funcionario(String nome, int max_diarias) {
		this.setNome(nome);
		this.setMax_diarias(max_diarias);
	}

	public void addDiaria() {
		
	}
	public String getNome() {
		return nome;
	}
	
	public int getMax_diarias() {
		return max_diarias;
	}
	
	public int getQtd_diarias() {
		return qtd_diarias;
	}
	
	public double getBonus() {
		return bonus;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void setMax_diarias(int max_diarias) {
		this.max_diarias = max_diarias;
	}
	
	public void setQtd_diarias(int qtd_diarias) {
		this.qtd_diarias = qtd_diarias;
	}
	
	public void setBonus(double bonus) {
		this.bonus = bonus;
	}
}
