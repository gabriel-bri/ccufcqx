package com.example;

import java.rmi.Remote;
import java.rmi.RemoteException;
// Interface remota que será usada pelo RMI
public interface Hello extends Remote {
   String sayHello(String name) throws RemoteException;
}
