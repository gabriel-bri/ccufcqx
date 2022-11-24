package model;

public class Marcador{
	private String label;

	public Marcador(String label){
		this.setLabel(label);
	}
	
	public void editar(String label){
		this.setLabel(label);
	}
	
	public String getLabel(){
		return label;
	}
	
	public void setLabel(String label) {
		this.label = label;
	}
	
	public String toString() {
		return getLabel();
	}
}