package control;

import model.Tarefa;
import model.Usuario;
import model.Marcador;
import view.Visao;

import java.util.ArrayList;
import java.util.Date;

import Exceptions.*;

public class ControleAtividades{
	private Usuario user;
	private Visao v;

  public ControleAtividades(Object O) throws ArgumentoInvalidoException{
	  super();
	  if(O instanceof Usuario) {
		  user = ((Usuario)O);
		  v = new Visao(user);
	  }
	  else {
		throw new ArgumentoInvalidoException();
	  }
    
  }

  public boolean addTarefa(Tarefa tarefa){
    try{
      user.criarTarefa(tarefa);
      return true;
    }
	
	catch(Exception e){
      System.out.print(e);
    }

    return false;
  }

  public boolean excluirTarefa(Object O) throws ArgumentoInvalidoException{
    if(O instanceof Tarefa) {
	      for(int i=0; i<user.getTask().size(); i++){
	        if(user.getTask().get(i).getLabel().equals(((Tarefa) O).getLabel())){
	          user.excluirTarefa(user.getTask().get(i));
	          return true;
	        }
	      }
	}

	else {
		throw new ArgumentoInvalidoException();
	}
    
	return false; 

  }

  public void alterardataconclusao(Object O, Date data) throws ArgumentoInvalidoException {
	  if(O instanceof Tarefa) {
		  for(Tarefa t : user.getTask()) {
			  if(t.getLabel().equals(((Tarefa) O).getLabel())) {
				t.setDataConclusao(data);
				return;
			  }
		  }
	  }
	  throw new ArgumentoInvalidoException();
  }

//Método que define a alteração da data lmite.
public void alterarDatalimite(Object O, Date data) throws ArgumentoInvalidoException {
	  if(O instanceof Tarefa) {
		  for(Tarefa t : user.getTask()) {
			  if(t.getLabel().equals(((Tarefa) O).getLabel())) {
				t.setDataLimite(data);
				return;
			  }
		  }
	  }
	  throw new ArgumentoInvalidoException();
}
  
  //Método que define a atividade como concluída. .
  public boolean concluirAtividade(Object O, boolean status) throws ArgumentoInvalidoException{
	  if(O instanceof Tarefa) {
		  ((Tarefa) O).concluir(); 
		  for(int i = 0; i < user.getTask().size(); i++) {
			if(user.getTask().get(i).getLabel().equals(((Tarefa) O).getLabel())){
				user.getTask().get(i).setConcluida(status);
				return true; 
			}
		  }
	  }

	  else {
		  throw new ArgumentoInvalidoException();
	  }

	  return false;
  }

  public boolean criarMarcador(Marcador marc){
    try{
      user.criarMarcador(marc);
    }
	
	catch(Exception e){
      System.out.print(e);
    }
    
	return false;
  }
  
  public Marcador buscarMarc(String nome) throws MarcadorInvalidoException {
	  ArrayList<Marcador> auxmarc = user.getMarcador();
	  for(int i=0; i<auxmarc.size(); i++) {
		  if(auxmarc.get(i).getLabel().equals(nome)) {
			  return auxmarc.get(i);
		  }  
	  }
	 
	  throw new MarcadorInvalidoException();
  }
  
  public void alterarMarc(Object O, String novo_marc) throws ArgumentoInvalidoException{
	  if(O instanceof Marcador) {
		  ((Marcador) O).setLabel(novo_marc);
	  }
	  
	  else {
			throw new ArgumentoInvalidoException();
	  }
  }
  
  public void excluiMarc(Object O) throws ArgumentoInvalidoException{
	  if(O instanceof Marcador) {
		  for(int i=0; i<user.getMarcador().size(); i++) {
			  if(user.getMarcador().get(i).equals(O)) {
				  user.excluiMarcador(user.getMarcador().get(i));
			  }
		  }
	  }

	  else {
		  throw new ArgumentoInvalidoException();
	  }
  }
  
  public Tarefa buscarTarefa(String nome) throws ArgumentoInvalidoException {
	ArrayList<Tarefa> auxTask = user.getTask();
	for(int i=0; i<auxTask.size(); i++) {
		if(auxTask.get(i).getLabel().equals(nome)) {
			return auxTask.get(i); 
		}
	}
	throw new ArgumentoInvalidoException();
  }
  
  public void alterarDesc(Object O, String nova_desc) throws ArgumentoInvalidoException{
	  if(O instanceof Tarefa) {
		  for(int i=0; i<user.getTask().size(); i++) {
			  if(user.getTask().get(i).getLabel().equals(((Tarefa) O).getLabel())) {
				  user.getTask().get(i).setDescricao(nova_desc);
				  return;
			  }
		  }
	  }
	  else {
			throw new ArgumentoInvalidoException();
	  }

  }
  
  public void associarMarcador(Object a, Object b) throws ArgumentoInvalidoException{
	  if(a instanceof Tarefa && b instanceof Marcador) {
		  user.associarMarcador(b, a);
	  }

	   else {
			throw new ArgumentoInvalidoException();
	  }
  }

	public Visao getV() {
		return v;
	}

	public void setV(Visao v) {
		this.v = v;
	}
 }