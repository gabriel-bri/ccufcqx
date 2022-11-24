package modelo;

public class Alongamento {
	private int codigo_de_plano;
	private boolean Alongamento_ParteSuperior_do_Corpo;
	private boolean Alongamento_Dor_nas_Costas;
	private boolean Alongamento_Parte_Inferior_do_Corpo;
	private boolean Postura_de_Crianca;
	private boolean Alongamento_peito;
	private boolean Alongamento_de_Ombros;
	private boolean Alongamento_Cobra;
	private boolean Alongamento_Triceps;
	private boolean Alongamento_Panturrilha;
	private int quem_pratica;
	
	public Alongamento() {
		
	}
	public Alongamento( int codigo_de_plano,
			 boolean alongamento_ParteSuperior_do_Corpo,
			 boolean alongamento_Dor_nas_Costas,
			 boolean alongamento_Parte_Inferior_do_Corpo,
			 boolean postura_de_Crianca,
			 boolean alongamento_peito,
			 boolean alongamento_de_Ombros,
			 boolean alongamento_Cobra,
			 boolean alongamento_Triceps,
			 boolean alongamento_Panturrilha,
			 int quem_pratica 
			) {
		this.setCodigo_de_plano(codigo_de_plano);
		this.setAlongamento_ParteSuperior_do_Corpo(alongamento_ParteSuperior_do_Corpo);
		this.setAlongamento_Dor_nas_Costas(alongamento_Dor_nas_Costas);
		this.setAlongamento_Parte_Inferior_do_Corpo(alongamento_Parte_Inferior_do_Corpo);
		this.setPostura_de_Crianca(postura_de_Crianca);
		this.setAlongamento_peito(alongamento_peito);
		this.setAlongamento_de_Ombros(alongamento_de_Ombros);
		this.setAlongamento_Cobra(alongamento_Cobra);
		this.setAlongamento_Triceps(alongamento_Triceps);
		this.setAlongamento_Panturrilha(alongamento_Panturrilha);
		this.setQuem_pratica(quem_pratica);
	}
	public int getCodigo_de_plano() {
		return codigo_de_plano;
	}
	
	public boolean isAlongamento_ParteSuperior_do_Corpo() {
		return Alongamento_ParteSuperior_do_Corpo;
	}
	public boolean isAlongamento_Dor_nas_Costas() {
		return Alongamento_Dor_nas_Costas;
	}
	public boolean isAlongamento_Parte_Inferior_do_Corpo() {
		return Alongamento_Parte_Inferior_do_Corpo;
	}
	public boolean isPostura_de_Crianca() {
		return Postura_de_Crianca;
	}
	public boolean isAlongamento_peito() {
		return Alongamento_peito;
	}
	public boolean isAlongamento_de_Ombros() {
		return Alongamento_de_Ombros;
	}
	public boolean isAlongamento_Cobra() {
		return Alongamento_Cobra;
	}
	public boolean isAlongamento_Triceps() {
		return Alongamento_Triceps;
	}
	public boolean isAlongamento_Panturrilha() {
		return Alongamento_Panturrilha;
	}
	public int getQuem_pratica() {
		return quem_pratica;
	}
	public void setCodigo_de_plano(int codigo_de_plano) {
		this.codigo_de_plano = codigo_de_plano;
	}
	public void setAlongamento_ParteSuperior_do_Corpo(boolean alongamento_ParteSuperior_do_Corpo) {
		Alongamento_ParteSuperior_do_Corpo = alongamento_ParteSuperior_do_Corpo;
	}
	public void setAlongamento_Dor_nas_Costas(boolean alongamento_Dor_nas_Costas) {
		Alongamento_Dor_nas_Costas = alongamento_Dor_nas_Costas;
	}
	public void setAlongamento_Parte_Inferior_do_Corpo(boolean alongamento_Parte_Inferior_do_Corpo) {
		Alongamento_Parte_Inferior_do_Corpo = alongamento_Parte_Inferior_do_Corpo;
	}
	public void setPostura_de_Crianca(boolean postura_de_Crianca) {
		Postura_de_Crianca = postura_de_Crianca;
	}
	public void setAlongamento_peito(boolean alongamento_peito) {
		Alongamento_peito = alongamento_peito;
	}
	public void setAlongamento_de_Ombros(boolean alongamento_de_Ombros) {
		Alongamento_de_Ombros = alongamento_de_Ombros;
	}
	
	public void setAlongamento_Cobra(boolean alongamento_Cobra) {
		Alongamento_Cobra = alongamento_Cobra;
	}
	
	public void setAlongamento_Triceps(boolean alongamento_Triceps) {
		Alongamento_Triceps = alongamento_Triceps;
	}
	
	public void setAlongamento_Panturrilha(boolean alongamento_Panturrilha) {
		Alongamento_Panturrilha = alongamento_Panturrilha;
	}
	public void setQuem_pratica(int quem_pratica) {
		this.quem_pratica = quem_pratica;
	}
	
	
	
}
