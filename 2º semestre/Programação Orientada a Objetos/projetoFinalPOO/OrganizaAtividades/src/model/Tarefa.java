package model;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.ArrayList;

public class Tarefa implements Comparable<Tarefa>{
	  private String descricao;
	  private Date dataLimite;
	  SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yyyy"); 
	  private Date dataConclusao;
	  private boolean concluida = false;
	  private String label;
	  private ArrayList<Marcador> marcadores;
    
	  public Tarefa(String label, String descricao, Date dataLimite){
      super();
	    this.label = label;
	    this.dataLimite = dataLimite;
	    this.dataConclusao = null;
      this.descricao = descricao;
      this.concluida = false;
	    marcadores = new ArrayList<Marcador>();
	  }

	  public void addMarcador(Object marcador){
	    marcadores.add((Marcador) marcador);
	  }

	  public void concluir(){
	    this.setConcluida(true);
	  }

	  public void editar(String label, String descricao, Date dataLimite){
	    this.label = label;
	    this.descricao = descricao;
	    this.dataLimite = dataLimite;
	  }

	  public void excluirMarcador(String label){
	    /*for(Marcador m : marcadores){
	      if(m.getLabel().equals(label)){
	        marcadores.remove(m);
	        return;
	      }
	    }*/
		  Marcador m = new Marcador(label);
		  marcadores.remove(m);
	    //System.out.println("Marcador nao encontrado");               
	  }

	  public String toString(){
	    String ret = "Marcadores: ";
	    for(Marcador m : marcadores){
	      ret+=m.getLabel();
	      ret+=", ";
	    }
	    ret+= "Label: "+getLabel()+" Descricao: "+getDescricao()+" dataLimite: "+ getDataLimite()+ "Data conclusao: "+getDataConclusao()+" Concluida: "+getConcluida();

	    return ret;
	  }
	  //getters e setters
	  public String getDescricao(){
	    return descricao;
	  }
	  public String getLabel(){
	    return label;
	  }
	  public Date getDataLimite(){
	    return dataLimite;
	  }
	  public Date getDataConclusao(){
	    return dataConclusao;
	  }

	  public boolean getConcluida(){
	    return concluida;
	  }
	  public String label(){
	    return label;
	  }

	  public void setDescricao(String descricao){
	    this.descricao = descricao;
	  }

	  public void setConcluida(boolean status){
	    this.concluida = status;
	  }

	  public void setLabel(String label){
	    this.label = label;
	  }

	public ArrayList<Marcador> getMarcadores() {
		return marcadores;
	}

	public void setMarcadores(ArrayList<Marcador> marcadores) {
		this.marcadores = marcadores;
	}

	public void setDataLimite(Date dataLimite) {
		this.dataLimite = dataLimite;
	}

	public void setDataConclusao(Date dataConclusao) {
		this.dataConclusao = dataConclusao;
	}

	@Override
	public int compareTo(Tarefa p2) {
		if(this.label.length() < p2.getLabel().length()) {
			return -1;
		}else if(this.label.length() > p2.getLabel().length()){
			return 1;
		}
		return 0;
	}
	  
}