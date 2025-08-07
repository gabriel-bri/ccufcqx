package com.example.Model;

public class Radio extends Aparelho implements Transferivel {
    private String faixaFrequencia;

    public Radio(String modelo, double preco, String faixaFrequencia) {
        super(modelo, preco);
        this.faixaFrequencia = faixaFrequencia;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("Rádio - Modelo: " + getModelo() + ", Preço: " + getPreco() + ", Faixa de Frequência: " + faixaFrequencia);
    }

    @Override
    public void transferir(String origem, String destino) {
        System.out.println("Transferindo Rádio de " + origem + " para " + destino);
    }
}