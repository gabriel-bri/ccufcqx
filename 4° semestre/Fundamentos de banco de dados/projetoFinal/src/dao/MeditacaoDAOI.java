package dao;

import java.util.List;

import modelo.Meditacao;


public interface MeditacaoDAOI {
	Meditacao get(int id);
	List<Meditacao> getAll();
	void save(Meditacao newm);
	void update(Meditacao newm, Meditacao oldm);
	void delete(int id);
	void deleteMeditacaoByUser(int id);
}
