package model;

import control.ArgumentoInvalidoException;
import control.ElementoRepetidoException;

public interface IRepositorio {
	public boolean add(Pessoa p) throws ElementoRepetidoException, ArgumentoInvalidoException;
	public boolean buscar(String chave) throws ArgumentoInvalidoException;
}

