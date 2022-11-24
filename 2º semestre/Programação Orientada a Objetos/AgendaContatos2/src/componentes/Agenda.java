package componentes;

import java.util.ArrayList;

public class Agenda {
	private ArrayList<Contato> contatos = new ArrayList<Contato>();
	
	public ArrayList<Contato> search (String pattern) {
		ArrayList<Contato> searched = new ArrayList<Contato>();
		
		for (Contato contato : getContatos()) {
			if (contato.getAllData().contains(pattern))
				searched.add(contato);
		}
		
		return searched;
	}
	
	public void addContato(String name, ArrayList<Fone> fones) {
		Contato contato = new Contato(name);
		int index = getContatosIndexByName(name);
		
		if (index == -1) {
			for (Fone fone : fones)
				contato.addFone(fone.getId(), fone.getNumber());

			contatos.add(contato);
		} else {
			Contato data = getContato(name);
			
			for (Fone fone : fones)
				data.addFone(fone.getId(), fone.getNumber());
			
			contatos.set(index, data);
		}
		
	}
	
	public ArrayList<Contato> getContatos () {
		return contatos;
	}
	
	public Contato getContato (String name) {
		int index = getContatosIndexByName(name);
		
		return (index != -1)? getContatos().get(index) : null;
	}

	public int getContatosIndexByName (String name) {
		int i = 0;
		
		for (Contato contato : getContatos()) {
			if (contato.getName().equals(name))
				return i;
			
			i++;
		}
		
		return -1;
	}
	

	public boolean rmContato(String name) {
		int index = getContatosIndexByName(name);
		
		if (index == -1)
			return false;
		else {
			contatos.remove(index);
			
			return true;
		}
	}
	
	@Override
	public String toString() {
		String contatosOrder = "";
		
		for (Contato contato : getContatos()) {
			contatosOrder += "- " + contato + "\n";
		}
		
		return contatosOrder;
	}	
}
