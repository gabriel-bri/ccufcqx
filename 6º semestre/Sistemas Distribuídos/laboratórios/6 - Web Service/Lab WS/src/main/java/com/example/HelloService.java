package com.example;

import javax.jws.WebMethod;
import javax.jws.WebService;
// Define o serviço web
@WebService
public interface HelloService {
   @WebMethod
   String sayHello(String name);
}

