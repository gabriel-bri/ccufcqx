package com.example.Model;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class ServidorTCP {
    public static void main(String[] args) {
        int porta = 5000;

        try (ServerSocket serverSocket = new ServerSocket(porta)) {
            System.out.println("Servidor aguardando conexões na porta " + porta);

            while (true) {
                try (Socket clientSocket = serverSocket.accept()) {
                    System.out.println("Conexão estabelecida com " + clientSocket.getInetAddress());

                    InputStream input = clientSocket.getInputStream();
                    receberDados(input);
                } catch (IOException e) {
                    System.err.println("Erro ao processar conexão do cliente: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao iniciar o servidor: " + e.getMessage());
        }
    }

    private static void receberDados(InputStream input) throws IOException {
        int numeroAparelhos = input.read();
        System.out.println("Número de aparelhos recebidos: " + numeroAparelhos);

        for (int i = 0; i < numeroAparelhos; i++) {
            int tamanhoModelo = input.read();
            byte[] modeloBytes = new byte[tamanhoModelo];
            input.read(modeloBytes);
            String modelo = new String(modeloBytes);

            int tamanhoPreco = input.read();
            byte[] precoBytes = new byte[tamanhoPreco];
            input.read(precoBytes);
            String preco = new String(precoBytes);

            System.out.println("Aparelho recebido - Modelo: " + modelo + ", Preço: " + preco);
        }
    }
}
