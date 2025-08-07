package com.example;

import java.util.List;

public class DepositoDTO {
    private String nome;
    private List<Aparelho> aparelhos;

    public DepositoDTO() {}

    public DepositoDTO(String nome, List<Aparelho> aparelhos) {
        this.nome = nome;
        this.aparelhos = aparelhos;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public List<Aparelho> getAparelhos() {
        return aparelhos;
    }

    public void setAparelhos(List<Aparelho> aparelhos) {
        this.aparelhos = aparelhos;
    }
}
