package com.example.Model;

public class DVDPlayer extends Aparelho implements Transferivel {
    public DVDPlayer(String modelo, double preco) {
        super(modelo, preco);
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("DVD Player - Modelo: " + getModelo() + ", Preço: " + getPreco());
    }

    @Override
    public void transferir(String origem, String destino) {
        System.out.println("Transferindo DVD Player de " + origem + " para " + destino);
    }
}