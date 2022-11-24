package dao;

import java.util.List;

import modelo.Yoga;

public interface YogaDAOI {
	Yoga get(int id);
	List<Yoga> getAll();
	void save(Yoga newy);
	void update(Yoga newy, Yoga oldy);
	void delete(int id);
	void deleteYogaByUser(int id);
}
