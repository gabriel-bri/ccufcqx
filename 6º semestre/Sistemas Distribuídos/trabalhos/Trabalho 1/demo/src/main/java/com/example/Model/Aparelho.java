package com.example.Model;

import java.io.Serializable;

public abstract class Aparelho implements Serializable {
    private String modelo;
    private double preco;

    public Aparelho(String modelo, double preco) {
        this.modelo = modelo;
        this.preco = preco;
    }

    public String getModelo() {
        return modelo;
    }

    public double getPreco() {
        return preco;
    }

    public abstract void exibirInformacoes();
}
