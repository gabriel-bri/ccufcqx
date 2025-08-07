import java.util.Scanner;

public class Main {
    
    public static void menu() {
        System.out.println("\nMENU");
        System.out.println("1 - Adicionar elemento");
        System.out.println("2 - Buscar elemento");
        System.out.println("3 - Excluir elemento");
        System.out.println("4 - Mostrar árvore");
        System.out.println("5 - Sair");
        System.out.print("Escolha uma opção: ");
    }

    public static void main(String[] args) {
        AvlTree arvore = new AvlTree();
        Scanner scanner = new Scanner(System.in);
        int opcao, chave;

        do {
            menu();
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite a chave a ser inserida: ");
                    chave = scanner.nextInt();

                    if (arvore.contains(chave)) {
                        System.out.println("Chave já existente na árvore! Não será inserida novamente.");
                    } else {
                        System.out.println("Inserindo " + chave);
                        arvore.add(chave);
                        arvore.bshow();
                        System.out.println("Chave inserida com sucesso.");
                    }
                    break;

                case 2:
                    System.out.print("Digite a chave a ser buscada: ");
                    chave = scanner.nextInt();
                    arvore.search_path(chave);
                    break;

                case 3:
                    System.out.print("Digite a chave a ser removida: ");
                    chave = scanner.nextInt();

                    if (arvore.remove(chave)) {
                        System.out.println("Chave removida com sucesso.");
                        arvore.bshow();
                    } else {
                        System.out.println("Chave não encontrada na árvore.");
                    }
                    break;

                case 4:
                    if (arvore.empty()) {
                        System.out.println("A árvore está vazia.");
                    } else {
                        System.out.println("\nÁrvore AVL:");
                        arvore.bshow();
                        System.out.println("Altura da arvore: " + arvore.height());
                    }
                    break;

                case 5:
                    System.out.println("Saindo...");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        } while (opcao != 5);

        scanner.close();
    }
}