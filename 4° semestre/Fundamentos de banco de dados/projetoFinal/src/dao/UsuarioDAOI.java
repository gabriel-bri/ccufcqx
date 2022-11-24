package dao;

import java.util.List;

import modelo.Usuario;

public interface UsuarioDAOI {
	Usuario get(int id);
	List<Usuario> getAll();
	void save(Usuario newu);
	void update(Usuario newu, Usuario oldu);
	void delete(int id);
	List<Usuario> usuariosMeditacoesDisponiveis();
	List<Usuario> usuariosMaiorNivelYoga();
}
