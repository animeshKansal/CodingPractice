package Animals;

public class Dog extends Animals {

	public Dog() {
		super(15);
		System.out.println("A dog has been created");
	}

	public void ruff() {
		System.out.println("Dog Says Ruff");
	}

	public void run() {
		System.out.println("A dog is running");
	}

}
