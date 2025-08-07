package com.example.Q3;

import java.io.*;
import java.net.Socket;

import com.example.Model.Aparelho;
import com.example.Model.TV;

public class Cliente {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 5000);
             ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream());
             ObjectInputStream in = new ObjectInputStream(socket.getInputStream())) {

            Aparelho tv = new TV("Samsung 4K", 2500.00, 55);

            System.out.println("Enviando requisição para o servidor...");
            out.writeObject(tv);
            out.flush();

            Aparelho aparelhoRecebido = (Aparelho) in.readObject();
            System.out.println("Resposta recebida do servidor:");
            aparelhoRecebido.exibirInformacoes();

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
