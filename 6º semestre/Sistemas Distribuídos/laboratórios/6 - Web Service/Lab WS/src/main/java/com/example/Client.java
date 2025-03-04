package com.example;

import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;
public class Client {
   public static void main(String[] args) {
       try {
           //URL do WSDL
           URL wsdlURL = new URL("http://localhost:8080/hello?wsdl");
           //Namespace e nome do serviço
           QName qname = new QName("http://exemplo.com/", "HelloServiceImplService");
           //Criação do serviço
           Service service = Service.create(wsdlURL, qname);
           HelloService hello = service.getPort(HelloService.class);
           //Chamada ao método remoto
           String response = hello.sayHello("Usuário");
           System.out.println("Resposta do servidor: " + response);
       } catch (Exception e) {
        e.printStackTrace();
       }
   }
}