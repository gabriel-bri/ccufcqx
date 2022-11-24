package util;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

	private static Connection con = null;

	static
	{
		String url = "jdbc:postgresql://localhost/projeto_final";
		String user = "postgres";
		String pass = "1234";
		try {
			Class.forName("org.postgresql.Driver");
			con = DriverManager.getConnection(url, user, pass);
		}
		catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
	}
	public static Connection getConnection()
	{
		return con;
	}
	
	public static void main(String[] args) {
		
		try {
			DatabaseConnection dbconexao = new DatabaseConnection();
			Connection con = dbconexao.getConnection();
			con.close();
			System.out.println("Desgraçaaaaaaaaaa");
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
}