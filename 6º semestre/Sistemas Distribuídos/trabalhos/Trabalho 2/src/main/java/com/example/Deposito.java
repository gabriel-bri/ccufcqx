package com.example;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Deposito extends UnicastRemoteObject implements Transferivel {
    private String nome;
    private List<Aparelho> aparelhos;

    public Deposito() throws RemoteException {
    }

    public Deposito(String nome) throws RemoteException {
        this.nome = nome;
        this.aparelhos = new ArrayList<>();
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

    public String toJSON() {
        try {
            ObjectMapper mapper = new ObjectMapper();
            DepositoDTO dto = new DepositoDTO(this.nome, this.aparelhos);
            return mapper.writeValueAsString(dto);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static Deposito fromJSON(String json) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            DepositoDTO dto = mapper.readValue(json, DepositoDTO.class);
            Deposito deposito = new Deposito(dto.getNome());
            deposito.aparelhos = dto.getAparelhos();
            return deposito;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    @Override
    public String toString() {
        return "Deposito{" +
                "nome='" + nome + '\'' +
                ", aparelhos=" + aparelhos +
                '}';
    }

    @Override
    public void transferirPara(String novoDeposito) {
        // Implementar a lógica de transferência
    }
}
