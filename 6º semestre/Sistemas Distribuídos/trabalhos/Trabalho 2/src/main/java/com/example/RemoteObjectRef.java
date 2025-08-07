package com.example;

import com.fasterxml.jackson.databind.ObjectMapper;

public class RemoteObjectRef {
    private String host;
    private int port;
    private String serviceName;

    public RemoteObjectRef() {
        // Construtor padrão
    }

    public RemoteObjectRef(String host, int port, String serviceName) {
        this.host = host;
        this.port = port;
        this.serviceName = serviceName;
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public String getServiceName() {
        return serviceName;
    }

    public void setServiceName(String serviceName) {
        this.serviceName = serviceName;
    }

    public String getUrl() {
        return "rmi://" + host + ":" + port + "/" + serviceName;
    }

    public String toJSON() {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.writeValueAsString(this);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static RemoteObjectRef fromJSON(String json) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(json, RemoteObjectRef.class);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
