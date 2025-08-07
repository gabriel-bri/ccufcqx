package com.example.Model;

import java.util.ArrayList;
import java.util.List;

public class Deposito {
    private String nome;
    private List<Aparelho> aparelhos;

    public Deposito(String nome) {
        this.nome = nome;
        this.aparelhos = new ArrayList<>();
    }

    public void adicionarAparelho(Aparelho aparelho) {
        aparelhos.add(aparelho);
        System.out.println(aparelho.getModelo() + " adicionado ao depósito " + nome);
    }

    public void listarAparelhos() {
        System.out.println("Depósito: " + nome);
        for (Aparelho aparelho : aparelhos) {
            aparelho.exibirInformacoes();
        }
    }

    public List<Aparelho> getAparelhos() {
        return aparelhos;
    }
}