import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Compagnia c1 = new Compagnia();
		Compagnia c2 = new Compagnia();
		Biglietteria b = new Biglietteria();
		b.aggiungi_compagnia(c1);
		b.aggiungi_compagnia(c2);
		c1.aggiungi_aereo(new Aereo("0001", 40));
		c1.aggiungi_aereo(new Aereo("0002", 10));
		c2.aggiungi_aereo(new Aereo("0003", 30));

		Scanner input = new Scanner(System.in);
		while (true) {
			LinkedList<Integer> posti = new LinkedList<Integer>();
			System.out.println("Operazioni disponibili:");
			System.out.println("1) Prenota posti");
			System.out.println("2) Visualizza posti disponibili");
			System.out.println("3) Esci");
			System.out.println();
			System.out.print("Cosa vuoi fare -> ");
			int scelta = input.nextInt();
			switch (scelta) {
			case 1:
				System.out.print("Inserisci codice aereo dove prenotare posti -> ");
				input.nextLine();
				String codice = input.nextLine();
				System.out.print("Inserisci il numero di posti da prenotare -> ");
				int nposti = input.nextInt();
				for (int i = 0; i < nposti; i++) {
					System.out.print("Inserisci posto da prenotare -> ");
					int posto = input.nextInt();
					posti.add(posto);

				}
				b.prenota(codice, posti);
				break;

			case 2:
				b.stampa();
				break;

			case 3:
				System.exit(0);
				break;
			default:
				System.out.println("Scelta non valida scegli un numero tra 1 e 3");
			}
			System.out.println();
		}
	}

}
