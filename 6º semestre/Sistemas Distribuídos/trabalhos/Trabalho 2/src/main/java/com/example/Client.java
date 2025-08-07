package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Client {
    public static void main(String[] args) {
        try {
            RemoteObjectRef ref = new RemoteObjectRef("localhost", 1099, "DepositoService");
            RequestHandler handler = new RequestHandler();
            ObjectMapper objectMapper = new ObjectMapper();

            Aparelho aparelho = new Radio("2", "Panasonic", 150.00, "FM 101.1");
            byte[] arguments = objectMapper.writeValueAsBytes(aparelho);
            handler.doOperation(ref, 1, arguments);

            byte[] response = handler.doOperation(ref, 3, new byte[0]);
            System.out.println(new String(response));

            handler.doOperation(ref, 2, arguments);

            response = handler.doOperation(ref, 3, new byte[0]);
            System.out.println(new String(response));

            String id = "2";
            response = handler.doOperation(ref, 4, id.getBytes());
            System.out.println(new String(response));

            String novoDeposito = "Novo Deposito";
            handler.doOperation(ref, 5, novoDeposito.getBytes());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
