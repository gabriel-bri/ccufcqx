package com.example.Model;

import java.io.Serializable;

public class Pessoa implements Serializable {
    private String nome;
    private String cpf;
    private int idade;

    public Pessoa(String nome, String cpf, int idade) {
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public int getIdade() {
        return idade;
    }
}
