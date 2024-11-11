
public class Main {

	public static void main(String[] args) {

		TriangoloRettangolo tr = new TriangoloRettangolo(1, 2);

		System.out.println(tr.Area());

		tr.setCat1(100);
		System.out.println(tr.Area());

		tr.setCat2(200);
		System.out.println(tr.Area());
		
		Persona pr = new Persona();
		pr.setNome("Ciccio");
		pr.setNome("Cicciolino");

		Persona pr1 = new Persona();
		pr1.setNome("Cioccio");

		pr1 = pr;

		pr = new Persona();
		pr.setNome("Ciaccio");
		
		pr1.setTemperaturaCelsius((float)37.5);

	}

}
