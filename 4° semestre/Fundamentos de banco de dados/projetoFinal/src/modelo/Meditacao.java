package modelo;

public class Meditacao {
	private int codigo_de_plano;
	private boolean Concentracao;
	private boolean Emocoes;
	private boolean Estresse;
	private int quem_pratica;
	
	public Meditacao() {
		
	}
	
	
	public Meditacao(int codigo_de_plano,
	 boolean concentracao,
	 boolean emocoes,
	 boolean estresse,
	 int quem_pratica) {
		this.setCodigo_de_plano(codigo_de_plano);
		this.setConcentracao(concentracao);
		this.setEmocoes(emocoes);
		this.setEstresse(estresse);
		this.setQuem_pratica(quem_pratica);
	}
	
	public int getCodigo_de_plano() {
		return codigo_de_plano;
	}
	public boolean isConcentracao() {
		return Concentracao;
	}
	public boolean isEmocoes() {
		return Emocoes;
	}
	public boolean isEstresse() {
		return Estresse;
	}
	public int getQuem_pratica() {
		return quem_pratica;
	}
	public void setCodigo_de_plano(int codigo_de_plano) {
		this.codigo_de_plano = codigo_de_plano;
	}
	public void setConcentracao(boolean concentracao) {
		Concentracao = concentracao;
	}
	public void setEmocoes(boolean emocoes) {
		Emocoes = emocoes;
	}
	public void setEstresse(boolean estresse) {
		Estresse = estresse;
	}
	public void setQuem_pratica(int quem_pratica) {
		this.quem_pratica = quem_pratica;
	}

	
	
}
