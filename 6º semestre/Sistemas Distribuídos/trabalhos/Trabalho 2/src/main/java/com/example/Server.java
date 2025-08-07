package com.example;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);
            Deposito deposito = new Deposito("Central");
            Radio radio = new Radio("1", "Sony", 99.99, "FM 100.1");
            deposito.adicionarAparelho(radio);
            Naming.rebind("rmi://localhost/DepositoService", deposito);
            System.out.println("Servidor pronto.");

            String json = deposito.toJSON();
            System.out.println(json);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
