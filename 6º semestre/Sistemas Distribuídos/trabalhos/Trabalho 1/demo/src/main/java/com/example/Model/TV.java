package com.example.Model;

public class TV extends Aparelho implements Transferivel {
    private int tamanhoTela;

    public TV(String modelo, double preco, int tamanhoTela) {
        super(modelo, preco);
        this.tamanhoTela = tamanhoTela;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("TV - Modelo: " + getModelo() + ", Preço: " + getPreco() + ", Tamanho da Tela: " + tamanhoTela + " polegadas.");
    }

    @Override
    public void transferir(String origem, String destino) {
        System.out.println("Transferindo TV de " + origem + " para " + destino);
    }
}