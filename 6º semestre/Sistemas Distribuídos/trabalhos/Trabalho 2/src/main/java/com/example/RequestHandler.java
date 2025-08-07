package com.example;

import java.rmi.Naming;
import com.fasterxml.jackson.databind.ObjectMapper;

public class RequestHandler {

    private ObjectMapper objectMapper = new ObjectMapper();

    public byte[] doOperation(RemoteObjectRef o, int methodId, byte[] arguments) {
        try {
            Transferivel remoteObject = (Transferivel) Naming.lookup(o.getUrl());
            String methodName = getMethodName(methodId);
            switch (methodName) {
                case "adicionarAparelho":
                    Aparelho aparelho = Aparelho.fromJSON(new String(arguments));
                    remoteObject.adicionarAparelho(aparelho);
                    break;
                case "removerAparelho":
                    Aparelho aparelhoToRemove = Aparelho.fromJSON(new String(arguments));
                    remoteObject.removerAparelho(aparelhoToRemove);
                    break;
                case "listarAparelhos":
                    return objectMapper.writeValueAsBytes(remoteObject.listarAparelhos());
                case "buscarAparelhoPorId":
                    String id = new String(arguments);
                    return objectMapper.writeValueAsBytes(remoteObject.buscarAparelhoPorId(id));
                case "transferirPara":
                    String novoDeposito = new String(arguments);
                    remoteObject.transferirPara(novoDeposito);
                    break;
                default:
                    throw new UnsupportedOperationException("Método não suportado: " + methodName);
            }
            return new byte[0];
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public byte[] getRequest() {
        try {
            String requestJson = "{ \"methodId\": 1, \"arguments\": \"{\\\"id\\\":\\\"1\\\",\\\"marca\\\":\\\"Sony\\\",\\\"preco\\\":99.99}\" }";
            return objectMapper.writeValueAsBytes(requestJson);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public void sendReply(byte[] reply, String clientUrl) {
        try {
            String jsonReply = new String(reply);
            Transferivel.fromJSON(jsonReply);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private String getMethodName(int methodId) {
        switch (methodId) {
            case 1:
                return "adicionarAparelho";
            case 2:
                return "removerAparelho";
            case 3:
                return "listarAparelhos";
            case 4:
                return "buscarAparelhoPorId";
            case 5:
                return "transferirPara";
            default:
                throw new IllegalArgumentException("Invalid methodId: " + methodId);
        }
    }
}
