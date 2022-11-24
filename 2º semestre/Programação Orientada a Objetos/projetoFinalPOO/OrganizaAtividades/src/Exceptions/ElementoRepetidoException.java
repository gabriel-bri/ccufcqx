package Exceptions;

@SuppressWarnings("serial")
public class ElementoRepetidoException extends Exception {
	@Override
	public String getMessage() {
		return "Elemento repetido, tente outro.";
	}
}