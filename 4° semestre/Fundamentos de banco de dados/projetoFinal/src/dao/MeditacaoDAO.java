package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import modelo.Meditacao;
import util.DatabaseConnection;

public class MeditacaoDAO implements MeditacaoDAOI{

	public DatabaseConnection db;

	@Override
	public Meditacao get(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "select * from meditacao_guiada where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			ResultSet res = st.executeQuery();
			
			if(res.next()) {
				
				Meditacao m = new Meditacao();
				
				m.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				m.setConcentracao(res.getBoolean("Concentracao"));
				m.setEmocoes(res.getBoolean("Emocoes"));
				m.setEstresse(res.getBoolean("Estresse"));
				m.setQuem_pratica(res.getInt("quem_pratica"));
				
				return m;
			}
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public List<Meditacao> getAll() {
		try {
			db = new DatabaseConnection();
			String sql = "select * from meditacao_guiada";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Meditacao> meditacoesList = new ArrayList<Meditacao>();
			
			while(res.next()) {
				Meditacao m = new Meditacao();
				
				m.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				m.setConcentracao(res.getBoolean("Concentracao"));
				m.setEmocoes(res.getBoolean("Emocoes"));
				m.setEstresse(res.getBoolean("Estresse"));
				m.setQuem_pratica(res.getInt("quem_pratica"));
				
				meditacoesList.add(m);
			}
			
			return meditacoesList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public void save(Meditacao newm) {
		try {
			db = new DatabaseConnection();
			String sql = "insert into meditacao_guiada values (default, ?, ?, ?, ?);";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newm.isConcentracao());
			st.setBoolean(2, newm.isEmocoes());
			st.setBoolean(3, newm.isEstresse());
			st.setInt(4, newm.getQuem_pratica());
			
			st.execute();			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	@Override
	public void update(Meditacao newm, Meditacao oldm) {
		try {
			db = new DatabaseConnection();
			String sql = "update meditacao_guiada set Concentracao = ?, Emocoes = ?, Estresse = ?"
					+ "where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newm.isConcentracao());
			st.setBoolean(2, newm.isEmocoes());
			st.setBoolean(3, newm.isEstresse());
			st.setInt(4, oldm.getCodigo_de_plano());
			
			st.execute();
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void delete(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "delete from meditacao_guiada where codigo_de_plano = ?";
			PreparedStatement st;
			st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			st.execute();

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	@Override
	public void deleteMeditacaoByUser(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "delete from meditacao_guiada where quem_pratica = ?";
			PreparedStatement st;
			st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			st.execute();

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	}

}
