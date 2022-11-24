package componentes;

public class STA extends Funcionario{
	
	private int nivel;

	STA(String nome, int nivel) {
		super(nome, 1);
		this.setNivel(nivel);
	}
	
	public double calcSalario() {
		return 3000 + (300 * this.getNivel());
	}
	
	public int getNivel() {
		return nivel;
	}

	public void setNivel(int nivel) {
		this.nivel = nivel;
	}
	
	
	
	
}
