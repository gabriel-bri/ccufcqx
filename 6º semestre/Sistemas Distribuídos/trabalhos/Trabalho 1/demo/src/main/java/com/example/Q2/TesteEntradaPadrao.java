package com.example.Q2;

import java.io.IOException;

public class TesteEntradaPadrao {
    public static void main(String[] args) {
        try {
            AparelhosInputStream inputStream = new AparelhosInputStream(System.in);
            System.out.println("Digite os dados dos aparelhos:");
            inputStream.lerAparelhos();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
