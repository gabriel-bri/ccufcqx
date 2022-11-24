package control;


import model.Pessoa;

import java.util.ArrayList;
import java.util.Iterator;

import model.IRepositorio;

public class RepositorioPessoa implements IRepositorio{
	public ArrayList<Pessoa> pessoas;
	
	public RepositorioPessoa() {
		super();
		this.pessoas = new ArrayList<Pessoa>();
	}
	
	@Override
	public boolean add(Pessoa p) throws ElementoRepetidoException, ArgumentoInvalidoException{	
		if(buscar(p.getNome())) {
			throw new ElementoRepetidoException();
		}
		
		else if(p.getIdade() < 0 || p.getNome().equals(" ")){
			throw new ArgumentoInvalidoException();
		}
		
		else {
			this.pessoas.add(p);
		}
		
		return true;
	}

	@Override
	public boolean buscar(String chave) throws ArgumentoInvalidoException{
		if(chave.equals(" ")) {
			throw new ArgumentoInvalidoException();
		}
		
		for (Iterator iterator = pessoas.iterator(); iterator.hasNext();) {
			Pessoa pessoa = (Pessoa) iterator.next();
			if(pessoa.getNome().equals(chave)) {
				return true;
			}
		}
		return false;
	}
	
	public void buscar2(String chave) throws ArgumentoInvalidoException{
		if(chave.equals(" ")) {
			throw new ArgumentoInvalidoException();
		}
		
		for (Iterator iterator = pessoas.iterator(); iterator.hasNext();) {
			Pessoa pessoa = (Pessoa) iterator.next();
			if(pessoa.getNome().equals(chave)) {
				System.out.println(pessoa.getNome() + " | " + pessoa.getIdade() + " anos");
			}
		}
	}

	@Override
	public String toString() {
		String resultados = "";
		
		for(int i = 0; i < this.pessoas.size(); i++) {
			resultados += this.pessoas.get(i).getNome() + "\n";
		}
		
		return resultados;
	}

	
	
	

}
