import java.util.ArrayList;
import java.util.List;

class Estoque {
    private List<Produto> produtos;

    public Estoque() {
        this.produtos = new ArrayList<>();
    }

    public void adicionarProduto(String nome, String tipo, int quantidade) {
        produtos.add(new Produto(nome, tipo, quantidade));
        System.out.println("Produto adicionado com sucesso!");
    }

    public void removerProduto(String nome) {
        produtos.removeIf(produto -> produto.getNome().equalsIgnoreCase(nome));
        System.out.println("Produto removido com sucesso!");
    }

    public void alterarQuantidade(String nome, int quantidade) {
        for (Produto produto : produtos) {
            if (produto.getNome().equalsIgnoreCase(nome)) {
                produto.setQuantidade(produto.getQuantidade() + quantidade);
                System.out.println("Quantidade alterada com sucesso!");
                return;
            }
        }
        System.out.println("Produto não encontrado!");
    }

    public void emitirRelatorio() {
        System.out.println("\n--- Relatório de Estoque ---");
        for (Produto produto : produtos) {
            System.out.println("Nome: " + produto.getNome() + ", Tipo: " + produto.getTipo() + ", Quantidade: " + produto.getQuantidade());
        }
    }

    public void emitirAvisoProdutosBaixos(int limite) {
        System.out.println("\n--- Produtos com Estoque Baixo ---");
        for (Produto produto : produtos) {
            if (produto.getQuantidade() < limite) {
                System.out.println("Nome: " + produto.getNome() + ", Quantidade: " + produto.getQuantidade());
            }
        }
    }

    public void pesquisarProduto(String nome) {
        for (Produto produto : produtos) {
            if (produto.getNome().equalsIgnoreCase(nome)) {
                System.out.println("Produto encontrado: " + produto.getNome() + " - Tipo: " + produto.getTipo() + " - Quantidade: " + produto.getQuantidade());
                return;
            }
        }
        System.out.println("Produto não encontrado!");
    }
}