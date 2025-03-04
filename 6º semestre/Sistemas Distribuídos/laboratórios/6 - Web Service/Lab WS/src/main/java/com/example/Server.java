package com.example;

import javax.xml.ws.Endpoint;
public class Server {
   public static void main(String[] args) {
       String url = "http://localhost:8080/hello";
       System.out.println("Publicando serviço em: " + url);
       //Publica o serviço
       Endpoint.publish(url, new HelloServiceImpl());
       System.out.println("Serviço Web pronto!");
   }
}
