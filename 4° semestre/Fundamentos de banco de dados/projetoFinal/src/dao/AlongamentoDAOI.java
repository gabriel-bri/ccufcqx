package dao;

import java.util.List;

import modelo.Alongamento;

public interface AlongamentoDAOI {
	Alongamento get(int id);
	List<Alongamento> getAll();
	void save(Alongamento newu);
	void update(Alongamento newa, Alongamento olda);
	void delete(int id);
	void deleteAlongamentoByUser(int id);
}
