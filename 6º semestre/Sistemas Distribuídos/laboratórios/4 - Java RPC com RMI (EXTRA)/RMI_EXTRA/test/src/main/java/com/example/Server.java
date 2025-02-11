package com.example;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
public class Server {
   public static void main(String[] args) {
       try {
           LocateRegistry.createRegistry(1099);

           HelloImpl hello = new HelloImpl();
           Naming.rebind("HelloService", hello);
       } catch (Exception e) {
           System.out.println("Trouble: " + e);
       }
   }
}
