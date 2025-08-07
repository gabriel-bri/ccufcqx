package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;

public class TV extends Aparelho {
    private int tamanhoTela;

    public TV() {
    }

    public TV(String id, String marca, double preco, int tamanhoTela) {
        super(id, marca, preco);
        this.tamanhoTela = tamanhoTela;
    }

    public int getTamanhoTela() {
        return tamanhoTela;
    }

    public void setTamanhoTela(int tamanhoTela) {
        this.tamanhoTela = tamanhoTela;
    }

    public String toJSON() {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.writeValueAsString(this);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static TV fromJSON(String json) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(json, TV.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public String toString() {
        return "TV{" + super.toString() + ", tamanhoTela=" + tamanhoTela + '}';
    }
}
