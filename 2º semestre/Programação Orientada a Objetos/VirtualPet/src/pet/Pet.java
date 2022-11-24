package pet;

public class Pet {

	private int energyMax;
	private int hungryMax;
	private int cleanMax;
	private int diamonds;
	private int energy;
	private int hungry;
	private int clean;
	private int age;
	private boolean alive;
	
	public Pet(int energyMax, int hungryMax, int cleanMax) {
		this.energyMax = energyMax;
		this.hungryMax = hungryMax;
		this.cleanMax = cleanMax;
		
		this.energy = this.energyMax;
		this.clean = this.cleanMax;
		this.alive = true;
	}	

	private void setEnergy(int energy) {
		this.energy += energy;
	}

	private void setHungry(int hungry) {
		this.hungry += hungry;
	}

	private void setClean(int clean) {
		this.clean += clean;
	}
		
	public int getEnergyMax() {
		return energyMax;
	}

	public int getHungryMax() {
		return hungryMax;
	}

	public int getCleanMax() {
		return cleanMax;
	}

	public int getDiamonds() {
		return diamonds;
	}

	public int getEnergy() {
		return energy;
	}

	public int getHungry() {
		return hungry;
	}

	public int getClean() {
		return clean;
	}

	public int getAge() {
		return age;
	}

	public boolean isAlive() {
		return alive;
	}

	//Metodos internos
	public void play() {
		if(this.getClean() <= 0 || this.getEnergy() <= 0 || this.getHungry() > 3) {
			this.alive = false;
			
			if(this.getHungry() > 3) {
				System.out.println("Seu pet morreu de fome");
			}
			
			if(this.getEnergy() <= 0) {
				System.out.println("Seu pet morreu sem energia");
			}
			
			if(this.getClean() <= 0) {
				System.out.println("Seu pet morreu sujo");
			}
		}
		
		else if(this.isAlive()) {
			this.diamonds += 1;
			this.setHungry(+1);
			this.setEnergy(-1);
			this.setClean(-1);
			System.out.println("Seu pet está brincando!");
		}
		
	}
	
	public void shower() {
		if(this.isAlive() != true) {
			System.out.println("Pet morreu, que péssimo dono que você é... grrrr");
		}
		
		else {
			System.out.println("Sep pet está tomando banho!");
			this.setClean(+1);
			this.setHungry(+1);
			this.setEnergy(-1);
		}
	}
	
	public void eat() {
		if(this.isAlive() != true) {
			System.out.println("Pet morreu, que péssimo dono que você é... grrrr");
		}
		
		else {
			System.out.println("Seu pet está comendo!");
			this.setEnergy(+1);
			this.setHungry(-1);
			this.setClean(-1);
		}
	}
	
	public void sleep() {
		if(this.isAlive() != true) {
			System.out.println("Pet morreu, que péssimo dono que você é... grrrr");
		}
		
		else {
			this.setEnergy(+1);
		}
	}	
	
	public void show() {
		System.out.println("---------------------------------------");
		System.out.println("Quantidade de diamantes de: " + this.getDiamonds());
		System.out.println("Quantade de energia de: " + this.getEnergy());
		System.out.println("Quantade de fome de: " + this.getHungry());
		System.out.println("Quantidade de limpeza de: " + this.getClean());
		System.out.println("Idade de: " + this.getAge());
     	System.out.println("Está vivo? " + ((this.isAlive() == true)? "Sim" : "Não"));
		this.age += 1;
		System.out.println("---------------------------------------");
	}
}
