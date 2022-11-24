package Exceptions;

@SuppressWarnings("serial")
public class ArgumentoInvalidoException extends Exception {
	@Override
	public String getMessage() {
		return "Argumento inválido, por favor, insira os dados corretamente.";
	}
}