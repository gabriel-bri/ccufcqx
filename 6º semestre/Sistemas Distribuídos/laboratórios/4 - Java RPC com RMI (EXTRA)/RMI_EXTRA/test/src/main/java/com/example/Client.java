package com.example;

import java.rmi.Naming;
public class Client {
   public static void main(String[] args) {
       try {

        Hello hello = (Hello) Naming.lookup("rmi://localhost:1099/HelloService");

           String response = hello.sayHello("Usuário");
           System.out.println("Resposta do servidor: " + response);
       } catch (Exception e) {
           System.out.println("Trouble: " + e);
       }
   }
}
