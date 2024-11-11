
public class Main {

	public static void main(String[] args) {
		Persona p1 = new Persona("mario", "rossi", "mrirss00E08H501P", 35, "via dei ciclamini 123", "+393491122334");
		System.out.println(p1);

		System.out.println(Somma(1, 2));
		System.out.println(Somma("1", "2"));

	}

	static int Somma(int a, int b) {
		return a + b;
	}

	static String Somma(String a, String b) {
		return a + b;
	}
}
