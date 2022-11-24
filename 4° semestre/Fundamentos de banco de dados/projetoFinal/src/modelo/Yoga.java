package modelo;

public class Yoga {
	private int codigo_de_plano;
	private boolean Concentracao_Mental;
	private boolean Aprimoramento_Mental;
	private boolean Encolhimento_dos_ombros;
	private boolean Inclinacao_para_os_lados;
	private boolean Postura_da_Esfinge;
	private boolean Ponte;
	private boolean Bananeira;
	private boolean Estocada_Crescente;
	private int quem_pratica;
	
	public Yoga() {
		
	}
	
	public Yoga(int codigo_de_plano,
			boolean concentracao_Mental,
			boolean aprimoramento_Mental,
			boolean encolhimento_dos_ombros,
			boolean inclinacao_para_os_lados,
			boolean postura_da_Esfinge,
			boolean ponte,
			boolean bananeira,
			boolean estocada_Crescente,
			int quem_pratica) {
		
		this.setCodigo_de_plano(codigo_de_plano);
		this.setConcentracao_Mental(concentracao_Mental);
		this.setAprimoramento_Mental(aprimoramento_Mental);
		this.setEncolhimento_dos_ombros(encolhimento_dos_ombros);
		this.setInclinacao_para_os_lados(inclinacao_para_os_lados);
		this.setPostura_da_Esfinge(postura_da_Esfinge);
		this.setPonte(ponte);
		this.setBananeira(bananeira);
		this.setQuem_pratica(quem_pratica);
	}
	
	public int getCodigo_de_plano() {
		return codigo_de_plano;
	}
	public boolean isConcentracao_Mental() {
		return Concentracao_Mental;
	}
	public boolean isAprimoramento_Mental() {
		return Aprimoramento_Mental;
	}
	public boolean isEncolhimento_dos_ombros() {
		return Encolhimento_dos_ombros;
	}
	public boolean isInclinacao_para_os_lados() {
		return Inclinacao_para_os_lados;
	}
	public boolean isPostura_da_Esfinge() {
		return Postura_da_Esfinge;
	}
	public boolean isPonte() {
		return Ponte;
	}
	public boolean isBananeira() {
		return Bananeira;
	}
	public boolean isEstocada_Crescente() {
		return Estocada_Crescente;
	}
	public void setCodigo_de_plano(int codigo_de_plano) {
		this.codigo_de_plano = codigo_de_plano;
	}
	public void setConcentracao_Mental(boolean concentracao_Mental) {
		Concentracao_Mental = concentracao_Mental;
	}
	public void setAprimoramento_Mental(boolean aprimoramento_Mental) {
		Aprimoramento_Mental = aprimoramento_Mental;
	}
	public void setEncolhimento_dos_ombros(boolean encolhimento_dos_ombros) {
		Encolhimento_dos_ombros = encolhimento_dos_ombros;
	}
	public void setInclinacao_para_os_lados(boolean inclinacao_para_os_lados) {
		Inclinacao_para_os_lados = inclinacao_para_os_lados;
	}
	public void setPostura_da_Esfinge(boolean postura_da_Esfinge) {
		Postura_da_Esfinge = postura_da_Esfinge;
	}
	public void setPonte(boolean ponte) {
		Ponte = ponte;
	}
	public void setBananeira(boolean bananeira) {
		Bananeira = bananeira;
	}
	public void setEstocada_Crescente(boolean estocada_Crescente) {
		Estocada_Crescente = estocada_Crescente;
	}
	public int getQuem_pratica() {
		return quem_pratica;
	}
	public void setQuem_pratica(int quem_pratica) {
		this.quem_pratica = quem_pratica;
	}
	
	
}
