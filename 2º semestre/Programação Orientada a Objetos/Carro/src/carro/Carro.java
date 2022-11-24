package carro;

public class Carro {
	public int gas;
	public int gasMax;
	public int pass;
	public int passMax;
	public int km;
	
	Carro() {
		this.setGas(100);
		this.setGasMax(100);
		this.setPass(2);
		this.setPassMax(2);
		this.setKm(0);
	}
	
	Carro(int pessoasMaxima, int kmAtual, int gasAtual) {
		this.setPassMax(pessoasMaxima);
		this.setKm(kmAtual);
		this.setGas(gasAtual);
	}

	public int getGas() {
		return gas;
	}

	public int getGasMax() {
		return gasMax;
	}

	public int getPass() {
		return pass;
	}

	public int getPassMax() {
		return passMax;
	}

	public int getKm() {
		return km;
	}

	public void setGas(int gas) {
		this.gas = gas;
	}

	public void setGasMax(int gasMax) {
		this.gasMax = gasMax;
	}

	public void setPass(int pass) {
		this.pass = pass;
	}

	public void setPassMax(int passMax) {
		this.passMax = passMax;
	}

	public void setKm(int km) {
		this.km = km;
	}
	
	public void in() {
		if(this.getPass() <= this.getPassMax()) {
			this.setPass(+1);
			System.out.println("Passageiro embarcado");
		}
		
		else {
			System.out.println("Não há espaço :/");
		}
	}
	
	public void out() {
		if(this.getPass() >= this.getPassMax()) {
			this.setPass(-1);
			System.out.println("Passageiro desembarcou");
		}
		
		else {
			System.out.println("Não há ninguém.");
		}
	}
	
	public void fuel(int value) {
		if(value + this.getGas() > this.getGasMax()) {
			this.setGas(100);
		}
		
		else {
			this.setGas(value + this.getGas());
		}
		
		System.out.println("Tanque cheio...");
	}
	
	public void drive(int distance) {
		if(this.pass >= 1 && this.getGas() > 0) {
			int distanceActual = distance;
			do {
				this.setKm(this.getKm() + 1);
				this.setGas(this.getGas() - 1);
				distanceActual -= 1;
				
				if(this.getGas() == 0) {
					System.out.println("Fail: Carro sem gasolina. Foi possível percorrer " + (distance - distanceActual));
				}
			}while(this.getGas() > 0 && distanceActual > 0);		
		}
		
		else {
			System.out.println("Sem passageiro ou gasolina :/");
		}
	}

	@Override
	public String toString() {
		return "Carro [gas=" + gas + ", pass=" + pass + ", km=" + km + "]";
	}
	
	
	
	
}
