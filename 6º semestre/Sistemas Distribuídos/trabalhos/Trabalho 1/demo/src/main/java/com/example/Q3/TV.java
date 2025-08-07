package com.example.Q3;

import com.example.Model.Aparelho;

public class TV extends Aparelho {
    private int tamanhoTela;

    public TV(String modelo, double preco, int tamanhoTela) {
        super(modelo, preco);
        this.tamanhoTela = tamanhoTela;
    }

    @Override
    public void exibirInformacoes() {
        System.out.println("TV - Modelo: " + getModelo() + ", Preço: " + getPreco() + ", Tamanho da Tela: " + tamanhoTela + " polegadas.");
    }
}

