package com.example.Q2;

import java.io.FileInputStream;
import java.io.IOException;

public class TesteArquivo {
    public static void main(String[] args) {
        try (FileInputStream fileIn = new FileInputStream("aparelhos.dat")) {
            AparelhosInputStream inputStream = new AparelhosInputStream(fileIn);
            inputStream.lerAparelhos();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
