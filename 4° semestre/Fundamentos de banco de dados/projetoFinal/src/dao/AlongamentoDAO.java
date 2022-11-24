package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import modelo.Alongamento;
import modelo.Usuario;
import util.DatabaseConnection;

public class AlongamentoDAO implements AlongamentoDAOI {

	public DatabaseConnection db;

	@Override
	public Alongamento get(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "select * from alongamento where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			ResultSet res = st.executeQuery();
			
			if(res.next()) {
				
				Alongamento al = new Alongamento();
				
				al.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				al.setAlongamento_ParteSuperior_do_Corpo(res.getBoolean("Alongamento_ParteSuperior_do_Corpo"));
				al.setAlongamento_Dor_nas_Costas(res.getBoolean("Alongamento_Dor_nas_Costas"));
				al.setAlongamento_Parte_Inferior_do_Corpo(res.getBoolean("Alongamento_Parte_Inferior_do_Corpo"));
				al.setPostura_de_Crianca(res.getBoolean("Postura_de_Crianca"));
				al.setAlongamento_peito(res.getBoolean("Alongamento_peito"));
				al.setAlongamento_de_Ombros(res.getBoolean("Alongamento_de_Ombros"));
				al.setAlongamento_Cobra(res.getBoolean("Alongamento_Cobra"));
				al.setAlongamento_Triceps(res.getBoolean("Alongamento_Triceps"));
				al.setAlongamento_Panturrilha(res.getBoolean("Alongamento_Panturrilha"));
				al.setQuem_pratica(res.getInt("quem_pratica"));
				
				return al;
			}
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public List<Alongamento> getAll() {
		try {
			db = new DatabaseConnection();
			String sql = "select * from alongamento";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Alongamento> alongamentosList = new ArrayList<Alongamento>();
			
			while(res.next()) {
				Alongamento al = new Alongamento();
				
				al.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				al.setAlongamento_ParteSuperior_do_Corpo(res.getBoolean("Alongamento_ParteSuperior_do_Corpo"));
				al.setAlongamento_Dor_nas_Costas(res.getBoolean("Alongamento_Dor_nas_Costas"));
				al.setAlongamento_Parte_Inferior_do_Corpo(res.getBoolean("Alongamento_Parte_Inferior_do_Corpo"));
				al.setPostura_de_Crianca(res.getBoolean("Postura_de_Crianca"));
				al.setAlongamento_peito(res.getBoolean("Alongamento_peito"));
				al.setAlongamento_de_Ombros(res.getBoolean("Alongamento_de_Ombros"));
				al.setAlongamento_Cobra(res.getBoolean("Alongamento_Cobra"));
				al.setAlongamento_Triceps(res.getBoolean("Alongamento_Triceps"));
				al.setAlongamento_Panturrilha(res.getBoolean("Alongamento_Panturrilha"));
				al.setQuem_pratica(res.getInt("quem_pratica"));
				
				alongamentosList.add(al);
			}
			
			return alongamentosList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public void save(Alongamento newa) {
		try {
			db = new DatabaseConnection();
			String sql = "insert into alongamento values (default, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newa.isAlongamento_ParteSuperior_do_Corpo());
			st.setBoolean(2, newa.isAlongamento_Dor_nas_Costas());
			st.setBoolean(3, newa.isAlongamento_Parte_Inferior_do_Corpo());
			st.setBoolean(4, newa.isPostura_de_Crianca());
			st.setBoolean(5, newa.isAlongamento_peito());
			st.setBoolean(6, newa.isAlongamento_de_Ombros());
			st.setBoolean(7, newa.isAlongamento_Cobra());
			st.setBoolean(8, newa.isAlongamento_Triceps());
			st.setBoolean(9, newa.isAlongamento_Panturrilha());
			st.setInt(10, newa.getQuem_pratica());
			
			st.execute();			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	@Override
	public void update(Alongamento newa, Alongamento olda) {
		try {
			db = new DatabaseConnection();
			String sql = "update alongamento set Alongamento_ParteSuperior_do_Corpo = ?, "
					+ " Alongamento_Dor_nas_Costas = ?, Alongamento_Parte_Inferior_do_Corpo = ?, "
					+ " Postura_de_Crianca = ?, Alongamento_peito = ?, Alongamento_de_Ombros = ?, "
					+ " Alongamento_Cobra = ? , Alongamento_Triceps = ?, Alongamento_Panturrilha = ? "
					+ "where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newa.isAlongamento_ParteSuperior_do_Corpo());
			st.setBoolean(2, newa.isAlongamento_Dor_nas_Costas());
			st.setBoolean(3, newa.isAlongamento_Parte_Inferior_do_Corpo());
			st.setBoolean(4, newa.isPostura_de_Crianca());
			st.setBoolean(5, newa.isAlongamento_peito());
			st.setBoolean(6, newa.isAlongamento_de_Ombros());
			st.setBoolean(7, newa.isAlongamento_Cobra());
			st.setBoolean(8, newa.isAlongamento_Triceps());
			st.setBoolean(9, newa.isAlongamento_Panturrilha());
			st.setInt(10, olda.getCodigo_de_plano());
			
			st.execute();
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	@Override
	public void delete(int id) {
		// TODO Auto-generated method stub
		try {
			db = new DatabaseConnection();
			String sql = "delete from alongamento where codigo_de_plano = ?";
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
	public void deleteAlongamentoByUser(int id) {
		// TODO Auto-generated method stub
		try {
			db = new DatabaseConnection();
			String sql = "delete from alongamento where quem_pratica = ?";
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
