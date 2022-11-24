package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import modelo.Yoga;
import util.DatabaseConnection;

public class YogaDAO implements YogaDAOI{

	public DatabaseConnection db;

	@Override
	public Yoga get(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "select * from yoga where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			ResultSet res = st.executeQuery();
			
			if(res.next()) {
				Yoga y = new Yoga();
				
				y.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				y.setConcentracao_Mental(res.getBoolean("Concentracao_Mental"));
				y.setAprimoramento_Mental(res.getBoolean("Aprimoramento_Mental"));
				y.setEncolhimento_dos_ombros(res.getBoolean("Encolhimento_dos_ombros"));
				y.setInclinacao_para_os_lados(res.getBoolean("Inclinacao_para_os_lados"));
				y.setPostura_da_Esfinge(res.getBoolean("Postura_da_Esfinge"));
				y.setPonte(res.getBoolean("Ponte"));
				y.setBananeira(res.getBoolean("Bananeira"));
				y.setEstocada_Crescente(res.getBoolean("Estocada_Crescente"));
				y.setQuem_pratica(res.getInt("quem_pratica"));
				
				return y;
			}
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public List<Yoga> getAll() {
		try {
			db = new DatabaseConnection();
			String sql = "select * from yoga";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Yoga> yogaList = new ArrayList<Yoga>();
			
			while(res.next()) {
				Yoga y = new Yoga();
				
				y.setCodigo_de_plano(res.getInt("codigo_de_plano"));
				y.setConcentracao_Mental(res.getBoolean("Concentracao_Mental"));
				y.setAprimoramento_Mental(res.getBoolean("Aprimoramento_Mental"));
				y.setEncolhimento_dos_ombros(res.getBoolean("Encolhimento_dos_ombros"));
				y.setInclinacao_para_os_lados(res.getBoolean("Inclinacao_para_os_lados"));
				y.setPostura_da_Esfinge(res.getBoolean("Postura_da_Esfinge"));
				y.setPonte(res.getBoolean("Ponte"));
				y.setBananeira(res.getBoolean("Bananeira"));
				y.setEstocada_Crescente(res.getBoolean("Estocada_Crescente"));
				y.setQuem_pratica(res.getInt("quem_pratica"));
				
				yogaList.add(y);
			}
			
			return yogaList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public void save(Yoga newy) {
		try {
			db = new DatabaseConnection();
			String sql = "insert into yoga values (default, ?, ?, ?, ?, ?, ?, ?, ?, ?);";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newy.isConcentracao_Mental());
			st.setBoolean(2, newy.isAprimoramento_Mental());
			st.setBoolean(3, newy.isEncolhimento_dos_ombros());
			st.setBoolean(4, newy.isInclinacao_para_os_lados());
			st.setBoolean(5, newy.isPostura_da_Esfinge());
			st.setBoolean(6, newy.isPonte());
			st.setBoolean(7, newy.isBananeira());
			st.setBoolean(8, newy.isEstocada_Crescente());
			st.setInt(9, newy.getQuem_pratica());
			
			st.execute();			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void update(Yoga newy, Yoga oldy) {
		try {
			db = new DatabaseConnection();
			String sql = "update yoga set Concentracao_Mental = ?, Aprimoramento_Mental = ?, Encolhimento_dos_ombros = ?,"
					+ " Inclinacao_para_os_lados = ?, Postura_da_Esfinge = ?, Ponte = ?, Bananeira = ?, Estocada_Crescente = ?"
					+ "where codigo_de_plano = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setBoolean(1, newy.isConcentracao_Mental());
			st.setBoolean(2, newy.isAprimoramento_Mental());
			st.setBoolean(3, newy.isEncolhimento_dos_ombros());
			st.setBoolean(4, newy.isInclinacao_para_os_lados());
			st.setBoolean(5, newy.isPostura_da_Esfinge());
			st.setBoolean(6, newy.isPonte());
			st.setBoolean(7, newy.isBananeira());
			st.setBoolean(8, newy.isEstocada_Crescente());
			st.setInt(9, oldy.getCodigo_de_plano());
			
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
			String sql = "delete from yoga where codigo_de_plano = ?";
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
	public void deleteYogaByUser(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "delete from yoga where quem_pratica = ?";
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
