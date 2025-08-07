package com.example.Q4;

import java.io.*;
import java.net.*;

public class ClientHandler implements Runnable {
    private Socket clientSocket;

    public ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            DataInputStream in = new DataInputStream(clientSocket.getInputStream());
            DataOutputStream out = new DataOutputStream(clientSocket.getOutputStream());

            String loginRequest = in.readUTF();
            boolean isAdmin = VotingServer.adminIds.contains(loginRequest);
            String loginResponse = isAdmin ? "Bem-vindo, Administrador!" : "Bem-vindo, Eleitor!";
            out.writeUTF(loginResponse);

            if (!isAdmin) {
                handleVoting(in, out);
            } else {
                handleAdminActions(in, out);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void handleVoting(DataInputStream in, DataOutputStream out) throws IOException {
        if (VotingServer.isVotingOpen()) {
            String candidates = String.join(", ", VotingServer.candidateList);
            out.writeUTF(candidates);

            String vote = in.readUTF();
            if (VotingServer.isVotingOpen()) {
                synchronized (VotingServer.votes) {
                    VotingServer.votes.put(vote, VotingServer.votes.getOrDefault(vote, 0) + 1);
                }
                out.writeUTF("Voto registrado com sucesso!");
            }
        } else {
            out.writeUTF("A votação foi encerrada. Não é possível votar.");
        }
    }

    private void handleAdminActions(DataInputStream in, DataOutputStream out) throws IOException {
        String actionRequest = in.readUTF();
        String[] actionParts = actionRequest.split(":");
        String action = actionParts[0];
        String candidate = actionParts[1];

        if ("add".equals(action)) {
            VotingServer.candidateList.add(candidate);
            out.writeUTF("Candidato adicionado com sucesso!");
        } else if ("remove".equals(action)) {
            VotingServer.candidateList.remove(candidate);
            out.writeUTF("Candidato removido com sucesso!");
        } else {
            out.writeUTF("Ação desconhecida.");
        }
    }
}
