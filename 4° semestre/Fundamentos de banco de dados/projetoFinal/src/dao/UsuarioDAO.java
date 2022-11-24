package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import modelo.Usuario;
import util.DatabaseConnection;

public class UsuarioDAO implements UsuarioDAOI {

	public DatabaseConnection db;
	
	@Override
	public Usuario get(int id) {
		try {
			db = new DatabaseConnection();
			String sql = "select * from usuarios where id=?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			ResultSet res = st.executeQuery();
			
			if(res.next()) {
				Usuario u = new Usuario();
				
				u.setId(res.getInt("id"));
				u.setNome(res.getString("nome"));
				u.setPeso(res.getDouble("peso"));
				u.setAltura(res.getDouble("altura"));
				
				return u;
			}
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public List<Usuario> getAll() {
		try {
			db = new DatabaseConnection();
			String sql = "select id, nome, peso, altura from usuarios";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Usuario> usuariosList = new ArrayList<Usuario>();
			
			while(res.next()) {
				Usuario u = new Usuario();
				u.setNome(res.getString("nome"));
				u.setId(res.getInt("id"));
				usuariosList.add(u);
			}
			
			return usuariosList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public void save(Usuario newu) {
		// TODO Auto-generated method stub

		try {
			db = new DatabaseConnection();
			String sql = "insert into usuarios values (default, ?, ?, ?);";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setString(1, newu.getNome());
			st.setDouble(2, newu.getPeso());
			st.setDouble(3, newu.getAltura());
			
			st.execute();			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void update(Usuario newu, Usuario oldu) {
		try {
			db = new DatabaseConnection();
			String sql = "update usuarios set nome = ?, peso = ?, altura = ? where id = ?";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			
			st.setString(1, newu.getNome());
			st.setDouble(2, newu.getPeso());
			st.setDouble(3, newu.getAltura());
			st.setInt(4, oldu.getId());
			
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
			String sql = " delete from relatorio_semana where qual_usuario = ?;"
					+ " delete from lembretes where qual_usuario = ?; "
					+ " delete from configuracoes_gerais where qual_usuario = ?;"
					+ " delete from usuarios where id = ?; ";
			PreparedStatement st;
			st = db.getConnection().prepareStatement(sql);
			st.setInt(1, id);
			st.setInt(2, id);
			st.setInt(3, id);
			st.setInt(4, id);
			st.execute();

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public List<Usuario> usuariosMeditacoesDisponiveis() {
		//Mostra quais usuarios realizaram as 3 meditações guiadas disponiveis.
		try {
			db = new DatabaseConnection();
			String sql = "select u.nome "
					+ "from meditacao_guiada "
					+ "INNER JOIN usuarios as u on u.id = meditacao_guiada.codigo_de_plano "
					+ "where concentracao = true and emocoes = true and estresse = true";
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Usuario> usuariosList = new ArrayList<Usuario>();
			
			while(res.next()) {
				Usuario u = new Usuario();
				u.setNome(res.getString("nome"));
				usuariosList.add(u);
			}
			
			return usuariosList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;
	}
	
	public List<Usuario> usuariosMaiorNivelYoga() {
		//Mostras quais usuarios realizaram as posturas com maior nível de dificuldade: Postura da Esfinge, Ponte e Bananeira.
		try {
			db = new DatabaseConnection();
			String sql = "select u.nome "
					+ "from yoga "
					+ "INNER JOIN usuarios as u on u.id = yoga.codigo_de_plano "
					+ "where postura_da_esfinge = true and ponte = true and bananeira = true";
			
			PreparedStatement st = db.getConnection().prepareStatement(sql);
			ResultSet res = st.executeQuery();
			List<Usuario> usuariosList = new ArrayList<Usuario>();
			
			while(res.next()) {
				Usuario u = new Usuario();
				u.setNome(res.getString("nome"));
				usuariosList.add(u);
			}
			
			return usuariosList;
			
 		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return null;		
	}
}
	