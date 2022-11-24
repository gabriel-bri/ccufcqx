package view;
import model.Usuario;
import Exceptions.*;

import model.Marcador;
public class Visao {
	private Usuario user;
	
	public Visao(Object O) throws ArgumentoInvalidoException{
		super();
		if(O instanceof Usuario){
			this.user = ((Usuario)O);
		}

		else {
			throw new ArgumentoInvalidoException();
		}
	}
	
	public void listarMarcadores() {
		System.out.println(user.getMarcador());
	}
	
	public String listarTarefas() {
		return user.listarTarefas();
	}
	
	public void listarTarefasporMarcador(Object O) throws ArgumentoInvalidoException{
		if(O instanceof Marcador) {
			for(int i=0; i<user.getTask().size(); i++) {
				if(user.getTask().get(i).getMarcadores().contains(O)) {
					System.out.println(user.getTask().get(i));
				}
			}
		}

		else {
			throw new ArgumentoInvalidoException();
		}
	}
}
