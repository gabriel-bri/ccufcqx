package com.example.Q2;

import java.io.IOException;
import java.io.InputStream;

public class AparelhosInputStream {
    private InputStream in;

    public AparelhosInputStream(InputStream in) {
        this.in = in;
    }

    public void lerAparelhos() throws IOException {

        int numeroAparelhos = in.read();
        System.out.println("Número de aparelhos recebidos: " + numeroAparelhos);

        for (int i = 0; i < numeroAparelhos; i++) {

            int tamanhoModelo = in.read();
            byte[] modeloBytes = new byte[tamanhoModelo];
            in.read(modeloBytes);
            String modelo = new String(modeloBytes);

            int tamanhoPreco = in.read();
            byte[] precoBytes = new byte[tamanhoPreco];
            in.read(precoBytes);
            String preco = new String(precoBytes);

            System.out.println("Aparelho recebido - Modelo: " + modelo + ", Preço: " + preco);
        }
    }
}

