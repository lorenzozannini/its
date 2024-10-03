
public class Cicli {

	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			System.out.println(i);
		}
		System.out.println("");
		System.out.println("");
		System.out.println("Tabellina del 7");
		for (int i = 7; i < 71; i += 7) {
			System.out.print(i+" ");
		}

		System.out.println("");
		System.out.println("");
		System.out.println("Tabellina del 7");
		for (int i = 1; i < 11; i++) {
			System.out.print(7 * i+" ");
		}
		
		System.out.println("");
		System.out.println("");
		System.out.println("Tabellina del 7");
		for (int i=1;i<11;i++) {
			int n=0;
			for (int k =1;k<=i;k++) {
				n+=7;
			}
			System.out.print(n+" ");
		}
	}

}
