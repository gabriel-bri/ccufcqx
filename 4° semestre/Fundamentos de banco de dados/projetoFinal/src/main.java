import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

import dao.AlongamentoDAO;
import dao.UsuarioDAO;
import modelo.Alongamento;
import modelo.Usuario;
import util.FuncoesMain;


public class main {
	public static void menu() {
		System.out.println("--------------------------------------------");
		System.out.println(" 		   MENU 					");
		System.out.println("--------------------------------------------");
		System.out.print("Digite o número para acessar a função:\n"
				+ "[ 0 ] - Para ver este menu a qaulquer momento.\n"
				+ "[ 1 ] - Para listar todos os usuários.\n"
				+ "[ 2 ] - Para atualizar um usuário.\n"
				+ "[ 3 ] - Para inserir um usuário.\n"
				+ "[ 4 ] - Para apagar um usuário.\n"
				+ "[ 5 ] - Mostra quais usuarios realizaram as 3 meditações guiadas disponiveis.\n"
				+ "[ 6 ] - Mostras quais usuarios realizaram as posturas com maior "
				+ "nível de dificuldade: Postura da Esfinge, Ponte e Bananeira.\n"
				+ "[ 7 ] - Listar alongamentos.\n"
				+ "[ 8 ] - Atualizar alongamentos.\n"
				+ "[ 9 ] - Inserir alongamentos.\n"
				+ "[ 10 ] - Apagar alongamentos.\n"
				+ "[ 11 ] - Listar meditações.\n"
				+ "[ 12 ] - Apagar meditações.\n"
				+ "[ 13 ] - Inserir meditações.\n"
				+ "[ 14 ] - Atualizar meditação.\n"
				+ "[ 15 ] - Listar yoga.\n"
				+ "[ 16 ] - Inserir yoga.\n"
				+ "[ 17 ] - Apagar yoga.\n"
				+ "[ 18 ] - Atualizar yoga.\n"
				+ "[ 99 ] - Para sair.\n");
	}
	
	public static void main(String[] args) throws SQLException {
		Scanner in = new Scanner(System.in);
		
		FuncoesMain funcoes = new FuncoesMain();
		
		int opt = -1;
		
		menu();
		
		while(opt != 99) {
			System.out.println("Digite a opção que você deseja:");
			opt = in.nextInt();
			
			if(opt == 0) {
				menu();
			}
			
			else if(opt == 1) {
				funcoes.listarUsuarios();
			}
			
			else if(opt == 2) {
				funcoes.atualizarUsuario();
			}
			
			else if(opt == 3) {
				funcoes.inserirUsuario();
			}
			
			else if(opt == 4) {
				funcoes.apagarUsuario();
			}
			
			else if(opt == 5) {
				funcoes.listaTresMeditacoesDisponives();
			}
			
			else if(opt == 6) {
				funcoes.listaUsuariosMaiorNivelYoga();
			}
			
			else if(opt == 7) {
				funcoes.listarAlongamentos();
			}
			
			else if(opt == 8) {
				funcoes.atualizarAlongamento();
			}
			
			else if(opt == 9) {
				funcoes.inserirAlongamentos();
			}
			
			else if(opt == 10) {
				funcoes.apagarAlongamento();
			}
			
			else if(opt == 11) {
				funcoes.listarMeditacoes();
			}
			
			else if(opt == 12) {
				funcoes.apagarMeditacao();
			}
			
			else if(opt == 13) {
				funcoes.inserirMeditacao();
			}
			
			else if(opt == 14) {
				funcoes.atualizarMeditacao();
			}
			
			else if(opt == 15) {
				funcoes.listarYoga();
			}
			
			else if(opt == 16) {
				funcoes.inserirYoga();
			}
			
			else if(opt == 17) {
				funcoes.apagarYoga();
			}
			
			else if(opt == 18) {
				funcoes.atualizarYoga();
			}
			
			else if(opt == 99) {
				funcoes.fecharConexoes();
				System.out.println("Até mais!");
			}
			
			else {
				System.out.println("Ops, a gente não conseguiu interpretar esse comando, pode tentar novamente?");
			}
		}
	}
}
