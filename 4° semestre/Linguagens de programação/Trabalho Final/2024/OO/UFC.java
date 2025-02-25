import java.util.Scanner;

public class UFC {
    public static void main(String[] args) {
        Estoque estoque = new Estoque();
        Scanner scanner = new Scanner(System.in);
        int opcao;

        estoque.adicionarProduto("Sabao", "Limpeza", 10);
        estoque.adicionarProduto("Limpol", "Limpeza", 5);
        estoque.adicionarProduto("Pincel", "Professores", 3);
        estoque.adicionarProduto("Clipes", "Secretarias", 50);
        estoque.adicionarProduto("Agua", "Consumo", 100);

        do {
            System.out.println("\n--- Sistema de Controle de Estoque UFC-Quixadá ---");
            System.out.println("1. Adicionar Produto");
            System.out.println("2. Remover Produto");
            System.out.println("3. Alterar Quantidade");
            System.out.println("4. Emitir Relatório");
            System.out.println("5. Aviso de Produtos com Estoque Baixo");
            System.out.println("6. Pesquisar Produto");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar o buffer

            switch (opcao) {
                case 1:
                    System.out.print("Digite o nome do produto: ");
                    String nome = scanner.nextLine();
                    System.out.print("Digite o tipo do produto (limpeza, professores, secretarias, consumo): ");
                    String tipo = scanner.nextLine();
                    System.out.print("Digite a quantidade: ");
                    int quantidade = scanner.nextInt();
                    estoque.adicionarProduto(nome, tipo, quantidade);
                    break;
                case 2:
                    System.out.print("Digite o nome do produto a ser removido: ");
                    nome = scanner.nextLine();
                    estoque.removerProduto(nome);
                    break;
                case 3:
                    System.out.print("Digite o nome do produto: ");
                    nome = scanner.nextLine();
                    System.out.print("Digite a quantidade a ser adicionada: ");
                    quantidade = scanner.nextInt();
                    estoque.alterarQuantidade(nome, quantidade);
                    break;
                case 4:
                    estoque.emitirRelatorio();
                    break;
                case 5:
                    System.out.print("Digite o limite para aviso de estoque baixo: ");
                    int limite = scanner.nextInt();
                    estoque.emitirAvisoProdutosBaixos(limite);
                    break;
                case 6:
                    System.out.print("Digite o nome do produto que deseja pesquisar: ");
                    nome = scanner.nextLine();
                    estoque.pesquisarProduto(nome);
                    break;
                case 0:
                    System.out.println("Saindo do sistema...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        scanner.close();
    }
}