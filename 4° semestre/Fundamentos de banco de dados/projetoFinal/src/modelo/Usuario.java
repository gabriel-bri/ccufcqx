package modelo;

public class Usuario {
	private int id;
	private String nome;
	private double peso;
	private double altura;
	
	public Usuario() {
		
	}
	
	public Usuario(String nome, double peso, double altura) {
		this.setNome(nome);
		this.setPeso(peso);
		this.setAltura(altura);
	}
	
	public Usuario(int id, String nome, double peso, double altura) {
		this.setId(id);
		this.setNome(nome);
		this.setPeso(peso);
		this.setAltura(altura);
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getId() {
		return id;
	}
	
	public double getPeso() {
		return peso;
	}
	
	public double getAltura() {
		return altura;
	}
	public void setId(int id) {
		this.id = id;
	}
	
	public void setPeso(double peso) {
		this.peso = peso;
	}
	
	public void setAltura(double altura) {
		this.altura = altura;
	}
	
	
}
