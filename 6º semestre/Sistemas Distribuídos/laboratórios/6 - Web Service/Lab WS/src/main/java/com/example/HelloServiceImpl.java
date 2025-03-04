package com.example;

import javax.jws.WebService;
// Implementa o serviço web
@WebService(endpointInterface = "com.exemplo.HelloService")
public class HelloServiceImpl implements HelloService {
   @Override
   public String sayHello(String name) {
       return "Olá, " + name + "! Bem-vindo ao Web Service SOAP.";
   }
}
