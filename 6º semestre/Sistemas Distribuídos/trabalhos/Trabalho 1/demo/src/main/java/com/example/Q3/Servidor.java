package com.example.Q3;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

import com.example.Model.Aparelho;

public class Servidor {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5000)) {
            System.out.println("Servidor aguardando conexões...");

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream());
                     ObjectOutputStream out = new ObjectOutputStream(clientSocket.getOutputStream())) {

                    Aparelho aparelhoRecebido = (Aparelho) in.readObject();
                    System.out.println("Requisição recebida:");
                    aparelhoRecebido.exibirInformacoes();

                    out.writeObject(aparelhoRecebido);
                    out.flush();
                    System.out.println("Resposta enviada de volta para o cliente.");

                } catch (IOException | ClassNotFoundException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
