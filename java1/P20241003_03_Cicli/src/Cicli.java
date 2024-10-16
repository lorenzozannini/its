import java.util.Scanner;

public class Cicli {

	public static void main(String[] args) {
		/*
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
		
		int n = 4;
		if (n % 2 == 0) {
			System.out.println(n + " è un numero pari");
		} else {
			System.out.println(n + " è un numero dispari");
		}
		*/
		Scanner leggi = new Scanner(System.in);
		
		for (int i=0;i<10;i++) {
			System.out.print("Inserisci numero-> ");
			int n=leggi.nextInt();
			if (n>10) {
				System.out.println("Numero maggiore di 10");
			}else{
				System.out.println("Numero minore di 10");
			}
		}
	}

}
