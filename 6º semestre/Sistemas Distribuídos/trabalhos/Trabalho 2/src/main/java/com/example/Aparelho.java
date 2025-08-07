package com.example;

import java.io.Serializable;
import java.util.Objects;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Aparelho implements Serializable {
    private String id;
    private String marca;
    private double preco;

    public Aparelho() {
    }

    public Aparelho(String id, String marca, double preco) {
        this.id = id;
        this.marca = marca;
        this.preco = preco;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
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

    public static Aparelho fromJSON(String json) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(json, Aparelho.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public String toString() {
        return "Aparelho{" +
                "id='" + id + '\'' +
                ", marca='" + marca + '\'' +
                ", preco=" + preco +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Aparelho aparelho = (Aparelho) o;
        return Objects.equals(id, aparelho.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
