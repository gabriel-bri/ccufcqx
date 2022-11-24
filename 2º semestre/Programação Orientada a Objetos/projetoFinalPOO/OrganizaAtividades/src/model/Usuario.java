package model;

import Exceptions.*;
import java.util.ArrayList;

public class Usuario {
	private String nome;
	private String senha;
	private String email;
    private ArrayList<Tarefa> task;
    private ArrayList<Marcador> marcador = new ArrayList<Marcador>();

  public Usuario(String nome, String email, String senha){
    super();
    this.nome = nome;
    this.senha = senha;
    this.email = email;
    task = new ArrayList<Tarefa>();
  }

	public void criarTarefa(Object O) throws ArgumentoInvalidoException{
		if(O instanceof Tarefa) {
			Tarefa t = new Tarefa((((Tarefa) O).getLabel()), ((Tarefa) O).getDescricao(),((Tarefa) O).getDataLimite());
      		task.add(t);
		}
    
    	else {
			throw new ArgumentoInvalidoException();
		}
	}
	
	public void excluirTarefa(Tarefa t){
		task.remove(t);
	}
	
	public void criarMarcador(Object O) throws ArgumentoInvalidoException{
		if(O instanceof Marcador){
      		Marcador m = new Marcador(((Marcador)O).getLabel());
      		marcador.add(m);
    	}
		
		else{
			throw new ArgumentoInvalidoException();
    	}
	}
	
	public void excluiMarcador(Object O) throws ArgumentoInvalidoException{
		if(O instanceof Marcador) {
			/*for(Marcador m : marcador) {
				if(m.getLabel().equals(((Marcador) O).getLabel())) {
					marcador.remove(m);
				}
			}*/
			if(marcador.contains(O))
				marcador.remove(O);
			
			for(Tarefa t : task) {
				if(t.getMarcadores().contains(O))
					t.getMarcadores().remove(O);
			}
			
		}
		else {
			throw new ArgumentoInvalidoException();
		}
	}
	
	public void associarMarcador(Object marcador, Object atividade) throws ArgumentoInvalidoException {
		if(marcador instanceof Marcador && atividade instanceof Tarefa){
			for(Tarefa t : task){
				if(t.getLabel().equals(((Tarefa)atividade).getLabel())){
					t.addMarcador(marcador);
				}
			}
		}
	
		else{
      		throw new ArgumentoInvalidoException();
    	}
	}
	
	public String listarTarefas() {
		String saida = "Tarefas[";
    	for(int i=0; i<task.size(); i++){
      		saida+=task.get(i);
      		saida+="\n";
    	}
    	
		saida+="]";
    	return saida;
	}
	 
	public String listarMarcador() {
		String saida = "Marcadores[";
		for(int i=0; i<marcador.size(); i++){
		saida+=task.get(i);
			if(i<marcador.size()-1)saida+=", ";
		}
		saida+="]";
		return saida;
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getSenha() {
		return senha;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
		
	public void setSenha(String senha) {
		this.senha = senha;
	}
	
	public void setEmail(String email) {
		this.email = email;
	}

	public ArrayList<Tarefa> getTask() {
		return task;
	}

	public void setTask(ArrayList<Tarefa> task) {
		this.task = task;
	}

	public ArrayList<Marcador> getMarcador() {
		return marcador;
	}

	public void setMarcador(ArrayList<Marcador> marcador) {
		this.marcador = marcador;
	}
	
}
