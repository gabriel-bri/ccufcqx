package util;

import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

import dao.AlongamentoDAO;
import dao.MeditacaoDAO;
import dao.UsuarioDAO;
import dao.YogaDAO;
import modelo.Alongamento;
import modelo.Meditacao;
import modelo.Usuario;
import modelo.Yoga;

public class FuncoesMain {
	
	//Cria os DAO
	UsuarioDAO usuario = new UsuarioDAO();
	AlongamentoDAO alongamento = new AlongamentoDAO();
	MeditacaoDAO meditacao = new MeditacaoDAO();
	YogaDAO yoga = new YogaDAO();
	Scanner in = new Scanner(System.in);
	
	public void listarUsuarios() {
		System.out.println("========================================");
		System.out.println("	Listando todos os usuários.		");
		System.out.println("========================================");
		
		List<Usuario> allUsuario = usuario.getAll();
		for(int i = 0; i < allUsuario.size(); i++) {
			Usuario u = allUsuario.get(i);

			System.out.println("ID do Usuário: " + u.getId() + " | Nome do usuário: " + u.getNome());
		}
	}
	
	public void atualizarUsuario() {
		System.out.print("Digite o ID do usuário que você deseja atualizar: ");
		int id = in.nextInt();
		
		try {
			Usuario u = usuario.get(id);
			
			if(u.getId() == id) {
				in.nextLine();
				System.out.print("Agora digite o novo nome: ");
				String nome = in.nextLine();
				System.out.print("\n");
				
				System.out.println("Agora digite o novo peso: ");
				double peso = in.nextDouble();
				
				System.out.println("Agora digite a nova altura: ");
				double altura = in.nextDouble();
				
				Usuario antigo = new Usuario(u.getId(), u.getNome(), u.getPeso(), u.getAltura());
				
				Usuario novo = new Usuario(u.getId(), nome, peso, altura);
				
				usuario.update(novo, antigo);
				
				System.out.println("O usuário foi atualizado com sucesso!");
			}
		}
		
		catch(Exception e) {
			System.out.println("Ops, nenhum usuário com este ID foi encontrado.");
		}
	}
	
	public void inserirUsuario() {
		try {
			System.out.print("Agora digite o novo nome: ");
			String nome = in.nextLine();
			System.out.print("\n");
			
			System.out.println("Agora digite o novo peso: ");
			double peso = in.nextDouble();
			
			System.out.println("Agora digite a nova altura: ");
			double altura = in.nextDouble();
			
			Usuario u = new Usuario(1, nome, peso, altura);
			
			usuario.save(u);
			
			System.out.println("Usuário inserido com sucesso!");
		}
		
		catch(Exception e) {
			System.out.println("Ops, tente novamente!");
		}
	}
	
	public void apagarUsuario() {
		System.out.println("Digite o ID do usuário a ser apagado: ");
		int id = in.nextInt();
		
		try {

			Usuario u = usuario.get(id);
			if(u.getId() == id) {
				
				alongamento.deleteAlongamentoByUser(id);
				meditacao.deleteMeditacaoByUser(id);
				yoga.deleteYogaByUser(id);
				
				usuario.delete(id);
				
				System.out.println("Usuário deletado com sucesso!");
			}
		}
		
		catch(Exception e) {
			System.out.println("Ops, a gente não encontrou esse usuário por aqui! :/");
		}
	}
	
	public void listaTresMeditacoesDisponives() {
		List<Usuario> allUsuario = usuario.usuariosMeditacoesDisponiveis();
		
		for(int i = 0; i < allUsuario.size(); i++) {
			Usuario u = allUsuario.get(i);

			System.out.println("Nome do usuário: " + u.getNome());
		}
	}
	
	public void listaUsuariosMaiorNivelYoga() {
		List<Usuario> allUsuario = usuario.usuariosMaiorNivelYoga();
		
		for(int i = 0; i < allUsuario.size(); i++) {
			Usuario u = allUsuario.get(i);

			System.out.println("Nome do usuário: " + u.getNome());
		}
	}
	
	//Funçoes para gerenciar alongamento.
	
	public void listarAlongamentos() {
		System.out.println("====================================================");
		System.out.println("	Listando todos os os planos de alongamento.		");
		System.out.println("====================================================");
		
		List<Alongamento> allAlongamento = alongamento.getAll();
		for(int i = 0; i < allAlongamento.size(); i++) {
			Alongamento a = allAlongamento.get(i);
			Usuario u = usuario.get(a.getQuem_pratica());
			
			System.out.print("ID do plano " + a.getCodigo_de_plano());
			System.out.print(" | Quem prstica? " + u.getNome());
			System.out.print(" | Alongamento parte superior: " + booleanParaTexto(a.isAlongamento_ParteSuperior_do_Corpo()));
			System.out.print(" | Alongamento dor nas costas: " + booleanParaTexto(a.isAlongamento_Dor_nas_Costas()));
			System.out.print(" | Alongamento parte inferior: " + booleanParaTexto(a.isAlongamento_Parte_Inferior_do_Corpo()));
			System.out.print(" | Posura de criança: " + booleanParaTexto(a.isPostura_de_Crianca()));
			System.out.print(" | Alongamento peito: " + booleanParaTexto(a.isAlongamento_peito()));
			System.out.print(" | Alongamento ombros: " + booleanParaTexto(a.isAlongamento_Cobra()));
			System.out.print(" | Alongamento cobra: " + booleanParaTexto(a.isAlongamento_Cobra()));
			System.out.print(" | Alongamento tríceps: " + booleanParaTexto(a.isAlongamento_Triceps()));
			System.out.print(" | Alongamento panturrilha: " + booleanParaTexto(a.isAlongamento_Panturrilha()));
			System.out.print("\n");
		}
	}
	
	public void atualizarAlongamento() {
		System.out.println("Digite o ID do plano de alongamento que você deseja atualizar:");

		int id = in.nextInt();

		try {
			Alongamento a = alongamento.get(id);
			
			if(a.getCodigo_de_plano() == id) {
				System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");
				
				System.out.println("Alongamento parte superior do corpo?");
				int op = in.nextInt();
				boolean alongamentoSuperior = intParaBoolean(op);
				
				System.out.println("Alongamento dor nas costas?");
				op = in.nextInt();
				boolean alongamentoCostas = intParaBoolean(op);
				
				System.out.println("Alongamento parte inferior do corpo?");
				op = in.nextInt();
				boolean alongamentoInferior = intParaBoolean(op);
				
				System.out.println("Postura de criança?");
				op = in.nextInt();
				boolean posturaCrianca = intParaBoolean(op);
				
				System.out.println("Alongamento peito?");
				op = in.nextInt();
				boolean alongamentoPeito = intParaBoolean(op);
				
				System.out.println("Alongamento ombros?");
				op = in.nextInt();
				boolean alongamentoOmbros = intParaBoolean(op);
				
				System.out.println("Alongamento cobra?");
				op = in.nextInt();
				boolean alongamentoCobra = intParaBoolean(op);
				
				System.out.println("Alongamento tríceps?");
				op = in.nextInt();
				boolean alongamentoTriceps = intParaBoolean(op);
				
				System.out.println("Alongamento panturrilha?");
				op = in.nextInt();
				boolean alongamentoPanturrilha = intParaBoolean(op);
				
				Alongamento antigo = new Alongamento(
						a.getCodigo_de_plano(),
						a.isAlongamento_ParteSuperior_do_Corpo(),
						a.isAlongamento_Dor_nas_Costas(),
						a.isAlongamento_Parte_Inferior_do_Corpo(),
						a.isPostura_de_Crianca(),
						a.isAlongamento_peito(),
						a.isAlongamento_de_Ombros(),
						a.isAlongamento_Cobra(),
						a.isAlongamento_Triceps(),
						a.isAlongamento_Panturrilha(),
						a.getQuem_pratica()
				);
				
				Alongamento novo = new Alongamento(
						a.getCodigo_de_plano(), 
						alongamentoSuperior, alongamentoCostas, alongamentoInferior,
						posturaCrianca, alongamentoPeito, alongamentoOmbros,
						alongamentoCobra, alongamentoTriceps, alongamentoPanturrilha,
						a.getQuem_pratica());
				
				alongamento.update(novo, antigo);
				
				System.out.println("O plano de alongamento foi atualizado com sucesso!");
			}
		}
		
		catch(Exception e) {
			System.out.println("Ops, nenhum plano com este ID foi encontrado.");
		}
	}
	
	public void inserirAlongamentos() {
		try {
			System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");
			
			System.out.println("Alongamento parte superior do corpo?");
			int op = in.nextInt();
			boolean alongamentoSuperior = intParaBoolean(op);
			
			System.out.println("Alongamento dor nas costas?");
			op = in.nextInt();
			boolean alongamentoCostas = intParaBoolean(op);
			
			System.out.println("Alongamento parte inferior do corpo?");
			op = in.nextInt();
			boolean alongamentoInferior = intParaBoolean(op);
			
			System.out.println("Postura de criança?");
			op = in.nextInt();
			boolean posturaCrianca = intParaBoolean(op);
			
			System.out.println("Alongamento peito?");
			op = in.nextInt();
			boolean alongamentoPeito = intParaBoolean(op);
			
			System.out.println("Alongamento ombros?");
			op = in.nextInt();
			boolean alongamentoOmbros = intParaBoolean(op);
			
			System.out.println("Alongamento cobra?");
			op = in.nextInt();
			boolean alongamentoCobra = intParaBoolean(op);
			
			System.out.println("Alongamento tríceps?");
			op = in.nextInt();
			boolean alongamentoTriceps = intParaBoolean(op);
			
			System.out.println("Alongamento panturrilha?");
			op = in.nextInt();
			boolean alongamentoPanturrilha = intParaBoolean(op);
			
			System.out.println("Agora digite o ID do usuário que fará este plano:");
			int idUsuario = in.nextInt();

			Alongamento a = new Alongamento(
					1, 
					alongamentoSuperior, alongamentoCostas, alongamentoInferior,
					posturaCrianca, alongamentoPeito, alongamentoOmbros,
					alongamentoCobra, alongamentoTriceps, alongamentoPanturrilha,
					idUsuario
			);
			
			alongamento.save(a);
			System.out.println("Plano inserido com sucesso!");
		}
		
		catch(Exception e) {
			System.out.println("Ops, tente novamente!");
		}
	}
	
	public void apagarAlongamento() {
		System.out.println("Digite o ID do plano a ser apagado");
		int id = in.nextInt();
		
		try {
			Alongamento a = alongamento.get(id);
			
			if(a.getCodigo_de_plano() == id) {
				alongamento.delete(id);
				
				System.out.println("Plano de alongamento deletado com sucesso!");
			}
			
		}
		
		catch(Exception e) {
			System.out.println("Ops, a gente não encontrou esse plano por aqui! :/");
		}
	}
	
	//Funçoes para gerenciar meditações
	public void listarMeditacoes() {
		System.out.println("================================================");
		System.out.println("	Listando todos os planos de meditação.		");
		System.out.println("================================================");
		
		List<Meditacao> allMeditacao = meditacao.getAll();
		for(int i = 0; i < allMeditacao.size(); i++) {
			Meditacao m = allMeditacao.get(i);
			
			Usuario u = usuario.get(m.getQuem_pratica());
			
			System.out.print("ID do plano " + m.getCodigo_de_plano());
			System.out.print(" | Quem prstica? " + u.getNome());
			System.out.print(" | Concentração: " + booleanParaTexto(m.isConcentracao()));
			System.out.print(" | Emoções: " + booleanParaTexto(m.isEmocoes()));
			System.out.print(" | Estresse: " + booleanParaTexto(m.isEstresse()));
			System.out.print("\n");
		}
	}
	
	public void apagarMeditacao() {
		System.out.println("Digite o ID do plano a ser apagado");
		int id = in.nextInt();
		
		try {
			Meditacao m = meditacao.get(id);
		
			if(m.getCodigo_de_plano() == id) {
				meditacao.delete(id);
				
				System.out.println("Plano de meditacão deletado com sucesso!");
			}
		}
		
		catch(Exception e) {
			System.out.println("Ops, a gente não encontrou esse plano por aqui! :/");
		}
	}
	
	public void inserirMeditacao() {
		try {
			System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");

			System.out.println("Concentração?");
			int op = in.nextInt();
			boolean concentracao = intParaBoolean(op);
			
			System.out.println("Emoções? ");
			op = in.nextInt();
			boolean emocoes = intParaBoolean(op);
			
			System.out.println("Estresse? ");
			op = in.nextInt();
			boolean estresse = intParaBoolean(op);
			
			System.out.println("Agora digite o ID do usuário que fará este plano:");
			int idUsuario = in.nextInt();
			
			Meditacao m = new Meditacao(1, concentracao, emocoes, estresse, idUsuario);
			
			meditacao.save(m);
			System.out.println("Plano inserido com sucesso!");
		}
		
		catch(Exception e) {
			System.out.println("Ops, tente novamente!");
		}
	}
	
	public void atualizarMeditacao() {
		System.out.println("Digite o ID do plano de meditação que você deseja atualizar:");
		int id = in.nextInt();
		
		try {
			Meditacao m = meditacao.get(id);
			
			if(m.getCodigo_de_plano() == id) {
				System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");

				System.out.println("Concentração?");
				int op = in.nextInt();
				boolean concentracao = intParaBoolean(op);
				
				System.out.println("Emoções? ");
				op = in.nextInt();
				boolean emocoes = intParaBoolean(op);
				
				System.out.println("Estresse? ");
				op = in.nextInt();
				boolean estresse = intParaBoolean(op);
				
				Meditacao antigo = new Meditacao(
						m.getCodigo_de_plano(),
						m.isConcentracao(),
						m.isEmocoes(),
						m.isEstresse(),
						m.getQuem_pratica()
				);
				
				Meditacao novo = new Meditacao(
						m.getCodigo_de_plano(), 
						concentracao, emocoes, estresse,
						m.getQuem_pratica());
				
				meditacao.update(novo, antigo);
				
				System.out.println("O plano de alongamento foi atualizado com sucesso!");
			}
			

		}
		
		catch(Exception e) {
			System.out.println("Ops, nenhum plano com este ID foi encontrado.");
		}		
	}
	
	//Yoga
	
	public void listarYoga() {
		System.out.println("================================================");
		System.out.println("	Listando todos os planos de yoga.		 ");
		System.out.println("================================================");
		
		List<Yoga> allYoga = yoga.getAll();
		for(int i = 0; i < allYoga.size(); i++) {
			Yoga y = allYoga.get(i);
			
			Usuario u = usuario.get(y.getQuem_pratica());
			
			System.out.print("ID do plano " + y.getCodigo_de_plano());
			System.out.print(" | Quem prstica? " + u.getNome());
			System.out.print(" | Concentração mental: " + booleanParaTexto(y.isConcentracao_Mental()));
			System.out.print(" | Aprimoramento mental: " + booleanParaTexto(y.isAprimoramento_Mental()));
			System.out.print(" | Encolhimentos dos ombros: " + booleanParaTexto(y.isEncolhimento_dos_ombros()));
			System.out.print(" | Inclinação para os lados: " + booleanParaTexto(y.isInclinacao_para_os_lados()));
			System.out.print(" | Postura de esfinge: " + booleanParaTexto(y.isPostura_da_Esfinge()	));
			System.out.print(" | Ponte: " + booleanParaTexto(y.isPonte()));
			System.out.print(" | Bananeira: " + booleanParaTexto(y.isBananeira()));
			System.out.print(" | Estocada crescente: " + booleanParaTexto(y.isEstocada_Crescente()));
			System.out.print("\n");
		}
	}
	
	public void inserirYoga() {
		try {
			System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");
			
			System.out.println("Concentração mental?");
			int op = in.nextInt();
			boolean concentracaoMental = intParaBoolean(op);

			System.out.println("Aprimoramento mental?");
			op = in.nextInt();
			boolean aprimoramentoMental = intParaBoolean(op);

			System.out.println("Encolhimento dos ombros?");
			op = in.nextInt();
			boolean encolhimentoOmbros = intParaBoolean(op);
			
			System.out.println("Inclinação para os lados?");
			op = in.nextInt();
			boolean inclinacaoLados = intParaBoolean(op);

			System.out.println("Postura de esfinge?");
			op = in.nextInt();
			boolean posturaEsfinge = intParaBoolean(op);
			
			System.out.println("Ponte?");
			op = in.nextInt();
			boolean ponte = intParaBoolean(op);
			
			System.out.println("Bananeira?");
			op = in.nextInt();
			boolean bananeira = intParaBoolean(op);
			
			System.out.println("Estocada crescente?");
			op = in.nextInt();
			boolean estocadaCrescente = intParaBoolean(op);

			System.out.println("Agora digite o ID do usuário que fará este plano:");
			int idUsuario = in.nextInt();
			
			Yoga y = new Yoga(1, concentracaoMental, aprimoramentoMental, encolhimentoOmbros, 
					inclinacaoLados, posturaEsfinge, ponte, bananeira, estocadaCrescente, idUsuario);
			
			yoga.save(y);
			System.out.println("Plano inserido com sucesso!");
		}
		
		catch(Exception e) {
			System.out.println("Ops, tente novamente!");
		}
	}
	
	public void apagarYoga() {
		System.out.println("Digite o ID do plano de yoga a ser apagado");
		int id = in.nextInt();
		
		try {

			Yoga y = yoga.get(id);
		
			if(y.getCodigo_de_plano() == id) {
				yoga.delete(id);
				
				System.out.println("Plano de yoga deletado com sucesso!");
			}
		}
		
		catch(Exception e) {
			System.out.println("Ops, a gente não encontrou esse plano por aqui! :/");
		}
	}

	public void atualizarYoga() {
		System.out.println("Digite o ID do plano de Yoga que você deseja atualizar:");
		int id = in.nextInt();
		
		try {
			
			Yoga y = yoga.get(id);
		
			if(y.getCodigo_de_plano() == id) {
				System.out.println("Agora digite os dados pedidos abaixo, sendo 1 para sim e 0 para não!");
				
				System.out.println("Concentração mental?");
				int op = in.nextInt();
				boolean concentracaoMental = intParaBoolean(op);

				System.out.println("Aprimoramento mental?");
				op = in.nextInt();
				boolean aprimoramentoMental = intParaBoolean(op);

				System.out.println("Encolhimento dos ombros?");
				op = in.nextInt();
				boolean encolhimentoOmbros = intParaBoolean(op);
				
				System.out.println("Inclinação para os lados?");
				op = in.nextInt();
				boolean inclinacaoLados = intParaBoolean(op);

				System.out.println("Postura de esfinge?");
				op = in.nextInt();
				boolean posturaEsfinge = intParaBoolean(op);
				
				System.out.println("Ponte?");
				op = in.nextInt();
				boolean ponte = intParaBoolean(op);
				
				System.out.println("Bananeira?");
				op = in.nextInt();
				boolean bananeira = intParaBoolean(op);
				
				System.out.println("Estocada crescente?");
				op = in.nextInt();
				boolean estocadaCrescente = intParaBoolean(op);
				
				Yoga antigo = new Yoga(
						y.getCodigo_de_plano(),
						y.isConcentracao_Mental(),
						y.isAprimoramento_Mental(),
						y.isEncolhimento_dos_ombros(),
						y.isInclinacao_para_os_lados(),
						y.isPostura_da_Esfinge(),
						y.isPonte(),
						y.isBananeira(),
						y.isEstocada_Crescente(),
						y.getQuem_pratica()
				);
				
				Yoga novo = new Yoga(y.getCodigo_de_plano(), concentracaoMental, aprimoramentoMental, encolhimentoOmbros, 
						inclinacaoLados, posturaEsfinge, ponte, bananeira, estocadaCrescente, y.getQuem_pratica());
				yoga.update(novo, antigo);
				
				System.out.println("O plano de yoga foi atualizado com sucesso!");				
			}

		}
		
		catch(Exception e) {
			System.out.println("Ops, nenhum plano com este ID foi encontrado.");
		}		
	}
	//Funçoes úteis
	public String booleanParaTexto(boolean valor) {
		if(valor) {
			return "Sim";
		}
		
		else {
			return "Não";
		}
	}
	
	public boolean intParaBoolean(int valor) {
		if(valor == 1) {
			return true;
		}
		
		else {
			return false;
		}
	}
	
	public void fecharConexoes() {
		try {
			usuario.db.getConnection().close();
			alongamento.db.getConnection().close();
			meditacao.db.getConnection().close();
			yoga.db.getConnection().close();
		} 
		
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
