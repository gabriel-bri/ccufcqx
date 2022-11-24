package componentes;

import java.util.ArrayList;

public class Contato {
	private String name;
	private ArrayList<Fone> fone;
	
	Contato(String name) {
		this.setName(name);
		this.fone = new ArrayList<Fone>();
	}
	
	public boolean addFone(String id, String number) {
		if(Fone.validate(number)) {		
			Fone f = new Fone(id, number);
			fone.add(f);
			return true;
		}
		
		else {
			return false;
		}
	}
	
	public String getAllData() {
		String fonesOrder = "";
		
		for (Fone fone : fone)
			fonesOrder += fone.getId()+":"+fone.getNumber()+" ";
		
		return name + fonesOrder;
	}
	
	public boolean rmFone(int id) {
		if(this.fone == null) {
			System.out.println("Sem dados cadastrados...");
			return false;
		}
		
		else {
			if(id >= fone.size() || fone.size() < 0) {
				System.out.println("Esse ID não conresponde a um contato válido");
				return false;
			}
			
			else {
				System.out.println("Contato removido!");
				fone.remove(id);
				return true;
			}
		}
	}

	public String getName() {
		return name;
	}

	private void setName(String name) {
		this.name = name;
	}
}
