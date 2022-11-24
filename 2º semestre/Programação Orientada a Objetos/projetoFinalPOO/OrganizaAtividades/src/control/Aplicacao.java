package control;

import model.Marcador;
import model.Tarefa;
import model.Usuario;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

import Exceptions.ArgumentoInvalidoException;

public class Aplicacao {
	public static void main(String[] args) throws ParseException, ArgumentoInvalidoException {
		SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yyyy");
		Scanner sc = new Scanner(System.in);
		Usuario user = new Usuario("","","");
		ControleAtividades controle = new ControleAtividades(user);
		
		
		System.out.println("Bem-vindo(a) ao Mural de Atividades!\n");
		System.out.println("Digite a opcao desejada:\n"
				+ "init - iniciar usuario (nome email senha)\n"
				+ "addTarefa - adicionar tarefa - (nome descricao data limite)\n"
				+ "altdesc - alterar descricao de uma tarefa(nome_tarefa nova_descricao)\n"
				+ "altdataconclusao - altera data de conclusao de uma tarefa (nome_tarefa nova_data)\n"
				+ "altdatalimite - altera data limite de uma tarefa (nome_tarefa nova_data)\n"
				+ "buscartarefa - busca uma tarefa com certo nome (nome_tarefa)\n"
				+ "concluitarefa - conclui uma tarefa (nome tarefa)\n"
				+ "excluitarefa - excluir tarefa (nome_tarefa)\n"
				+ "addmarc - adicionar marcador (nome_marcador)\n"
				+ "altmarc - alterar marcador (nome_marcador novo_nome_marcador)\n"
				+ "excluimarcador - excluir marcador (nome_marcador)\n"
				+ "assmarcador - associa marcador a uma atividade (nome_marcador nome_atividade)\n"
				+ "showAllTask - mostra todas as atividades do usuario\n"
				+ "showMarc - mostra todas as tarefas com um marcador (nome_marcadir)\n"
				+ "showallMarc - mostra todos os marcadores\n");
		
		String opc;
		boolean end = false;
		while(!end) {
			opc = sc.next();
			switch(opc) {
			case "init":
				String nome = sc.next();
				String email = sc.next();
				String senha = sc.next();
				try {
					user = new Usuario(nome, email, senha);
					controle = new ControleAtividades(user);
				}catch(Exception e) {
					System.out.println("Argumento invalido!");
				}
			break;

			case "addTarefa":
				String label = sc.nextLine();
				String descricao = sc.nextLine();
				String data = sc.next();
				Date date = formato.parse(data);
				try {
					Tarefa tarefa = new Tarefa(label, descricao, date);
					controle.addTarefa(((Tarefa)tarefa));
				}catch(Exception e) {
					System.out.println(e);
				}
			break;
			case "altdesc": 
				String nome_tarefa = sc.nextLine();
				String nova_desc = sc.nextLine();
				try {
				Tarefa t = controle.buscarTarefa(nome_tarefa);
				controle.alterarDesc(t, nova_desc);;
				}catch(Exception e) {
					System.out.println(e);
				}
				
			break;
			case "concluitarefa":
				String name_tarefa = sc.nextLine();
				String status = sc.nextLine();
				boolean s = true;
				if(status.equals("finalizar")) {
					s = true;
				}else if(status.equals("abrir")) {
					s = false;
				}
				try {
					Tarefa t = controle.buscarTarefa(name_tarefa);
					controle.concluirAtividade(t, s);
				}catch(Exception e) {
					System.out.println(e);
				}

			break;
			case "buscartarefa":
				String x = sc.nextLine();
				try {
					Tarefa t = controle.buscarTarefa(x);
					System.out.println(t);
				}catch (Exception e) {
					System.out.println(e);
				}
				
			break;
			case "altdataconclusao":
				String y = sc.nextLine();
				String dataconc = sc.nextLine();
				Date dataconcluir = formato.parse(dataconc);
				try {
					Tarefa t = controle.buscarTarefa(y);
					controle.alterardataconclusao(t, dataconcluir);
				}catch (Exception e) {
					System.out.println(e);
				}
				
			break;
			case "altdatalimite":
				String z = sc.nextLine();
				String datalimit = sc.nextLine();
				Date datalim = formato.parse(datalimit);
				try {
					Tarefa t = controle.buscarTarefa(z);
					controle.alterarDatalimite(t, datalim);
				}catch (Exception e) {
					System.out.println(e);
				}
				
			break;
			case "excluitarefa":
				String nome_exclui = sc.nextLine();
				try {
					Tarefa task = controle.buscarTarefa(nome_exclui);
					controle.excluirTarefa(task); 
					
				}catch(Exception e) {
					System.out.println(e);
				}
				
			break;
			case "addmarc":
				String n = sc.next();
				try {
					Marcador m = new Marcador(n);
					controle.criarMarcador(m);
				}catch(Exception e) {
					System.out.println(e);
				}
				break;
			case "altmarc":
				String marc = sc.next();
				String novo_marc = sc.next();
				try {
					Marcador m = controle.buscarMarc(marc);
					controle.alterarMarc(m, novo_marc);
				}catch(Exception e) {
					System.out.println(e);
				}
			break;
			case "excluimarcador":
				String n_marc = sc.next();
				try {
					Marcador m = controle.buscarMarc(n_marc);
					controle.excluiMarc(m);
				}catch(Exception e) {
					System.out.println(e);
				}
			break;
			case "assmarcador":
				String nome_task = sc.nextLine();
				String nome_marc = sc.nextLine();
				try {
					Tarefa ta = controle.buscarTarefa(nome_task);
					Marcador m = controle.buscarMarc(nome_marc);
					controle.associarMarcador(ta, m);
				}catch(Exception e) {
					System.out.println(e);
				}
				
			break;
			case "showMarc":
				String marcs = sc.next();
				try {
					Marcador m = controle.buscarMarc(marcs);
					controle.getV().listarTarefasporMarcador(m);
				}catch(Exception e) {
					System.out.println(e);
				}
				
			break;
			
			case "showallMarc":
				controle.getV().listarMarcadores();
			break;
			
			case "showallTask":
				System.out.println(controle.getV().listarTarefas());
			break;
			case "sair":
				end = true;
			break;
			}
		}
		sc.close();
	}
}
