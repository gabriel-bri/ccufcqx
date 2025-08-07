package com.example.Q2;

import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

public class TesteServidorTCP {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 5000)) {
            InputStream socketIn = socket.getInputStream();
            AparelhosInputStream inputStream = new AparelhosInputStream(socketIn);
            inputStream.lerAparelhos();
        } catch (IOException e) {
            System.err.println("Erro ao conectar ao servidor TCP. Certifique-se de que ele está em execução.");
            e.printStackTrace();
        }
    }
}

