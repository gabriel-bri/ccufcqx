package Exceptions;

@SuppressWarnings("serial")
public class MarcadorInvalidoException extends Exception {
	@Override
	public String getMessage() {
		return "Nenhum marcador com o nome repassado por você foi encontrado.";
	}
}