package com.example.Model;

import java.io.IOException;
import java.io.OutputStream;
import java.util.List;

public class AparelhosOutputStream {
    private OutputStream out;
    private List<Aparelho> aparelhos;

    public AparelhosOutputStream(OutputStream out, List<Aparelho> aparelhos) {
        this.out = out;
        this.aparelhos = aparelhos;
    }

    public void enviarAparelhos() throws IOException {
        out.write(aparelhos.size());

        for (Aparelho aparelho : aparelhos) {
            byte[] modeloBytes = aparelho.getModelo().getBytes();
            byte[] precoBytes = String.valueOf(aparelho.getPreco()).getBytes();

            out.write(modeloBytes.length);
            out.write(modeloBytes);

            out.write(precoBytes.length);
            out.write(precoBytes);
        }

        out.flush();
    }
}
