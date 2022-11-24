package componentes;

public class Fone {
	public String id;
	public String number;
	
	Fone(String id, String number) {
		this.setId(id);
		this.setNumber(number);
	}
	
	Fone(String serial) {
		String[] data = serial.split(":");
		
		this.setId(data[0]);
		this.setNumber(data[1]);
	}
	
	public static boolean validate(String number) {
		return number.matches("^\\([1-9]{2}\\) (?:[2-8]|9[1-9])[0-9]{3}\\-[0-9]{4}$");
	}

	public String getId() {
		return id;
	}

	private void setId(String id) {
		this.id = id;
	}

	public String getNumber() {
		return number;
	}

	private void setNumber(String number) {
		this.number = number;
	}

	@Override
	public String toString() {
		return "Fone [id=" + id + ", number=" + number + "]";
	}
}
