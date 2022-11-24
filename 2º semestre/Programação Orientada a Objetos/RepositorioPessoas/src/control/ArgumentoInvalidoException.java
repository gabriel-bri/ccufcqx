package control;

public class ArgumentoInvalidoException extends Exception {
	@Override
	public String getMessage() {
		return "Passagem de parâmetro inválida";
	}
	
}