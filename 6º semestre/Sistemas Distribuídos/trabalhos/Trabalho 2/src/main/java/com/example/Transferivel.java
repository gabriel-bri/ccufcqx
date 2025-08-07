package com.example;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;

public interface Transferivel extends Remote {
    void adicionarAparelho(Aparelho aparelho) throws RemoteException;

    void removerAparelho(Aparelho aparelho) throws RemoteException;

    List<Aparelho> listarAparelhos() throws RemoteException;

    Aparelho buscarAparelhoPorId(String id) throws RemoteException;

    void transferirPara(String novoDeposito) throws RemoteException;

    String toJSON() throws RemoteException;

    static Transferivel fromJSON(String json) throws RemoteException {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(json, Transferivel.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
