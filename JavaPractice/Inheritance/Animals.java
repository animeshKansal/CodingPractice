package Animals;

public class Animals {
	public int age;

	public Animals(int Age) {
		this.age = Age;
		System.out.println("An animal is created");
	}

	public void eat() {
		System.out.println("An animal is eating");
	}

	public static void main(String[] args) {
		Animals a = new Animals(5);
		Dog d = new Dog();
		cat c = new cat();
		d.ruff();
		c.meow();
		a.eat();
		d.eat();
		c.eat();
		d.run();
		c.prance();
	}

}
