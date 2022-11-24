package componentes;

public class Terceirizado extends Funcionario{
	
	private int horas_trab;
	private boolean insalubre;
	
	Terceirizado(String nome, int horas_trab, boolean insalubre) {
		super(nome, 0);
		this.setHoras_trab(horas_trab);
		this.setInsalubre(insalubre);
	}
	
	public int getHoras_trab() {
		return horas_trab;
	}
	
	public boolean isInsalubre() {
		return insalubre;
	}
	
	public void setHoras_trab(int horas_trab) {
		this.horas_trab = horas_trab;
	}
	
	public void setInsalubre(boolean insalubre) {
		this.insalubre = insalubre;
	}
	
	
}
