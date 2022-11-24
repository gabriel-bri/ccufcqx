package model;

public class Pessoa {
	private String nome;
	private int idade;
	
	public Pessoa(String nome, int idade) {
		this.setNome(nome);
		this.setIdade(idade);
	}

	public String getNome() {
		return nome;
	}

	public int getIdade() {
		return idade;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	
}
