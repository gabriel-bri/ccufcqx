package control;

public class ElementoRepetidoException extends Exception {
	@Override
	public String getMessage() {
		return "Elemento repetido.";
	}
}