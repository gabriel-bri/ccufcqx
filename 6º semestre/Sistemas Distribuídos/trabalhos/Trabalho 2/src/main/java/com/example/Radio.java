package com.example;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Radio extends Aparelho implements Transferivel {
    private String frequencia;
    private List<Aparelho> aparelhos = new ArrayList<>();

    public Radio() {
    }

    public Radio(String id, String marca, double preco, String frequencia) {
        super(id, marca, preco);
        this.frequencia = frequencia;
    }

    public String getFrequencia() {
        return frequencia;
    }

    public void setFrequencia(String frequencia) {
        this.frequencia = frequencia;
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

    public static Radio fromJSON(String json) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(json, Radio.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public String toString() {
        return "Radio{" + super.toString() + ", frequencia='" + frequencia + '\'' + '}';
    }

    @Override
    public void transferirPara(String novoDeposito) {
        System.out.println("Transferindo rádio para " + novoDeposito);
    }

    @Override
    public void adicionarAparelho(Aparelho aparelho) throws RemoteException {
        this.aparelhos.add(aparelho);
    }

    @Override
    public void removerAparelho(Aparelho aparelho) throws RemoteException {
        this.aparelhos.remove(aparelho);
    }

    @Override
    public List<Aparelho> listarAparelhos() throws RemoteException {
        return this.aparelhos;
    }

    @Override
    public Aparelho buscarAparelhoPorId(String id) throws RemoteException {
        for (Aparelho aparelho : aparelhos) {
            if (aparelho.getId().equals(id)) {
                return aparelho;
            }
        }
        return null;
    }
}
