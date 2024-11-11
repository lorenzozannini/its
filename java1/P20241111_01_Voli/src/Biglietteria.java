import java.util.LinkedList;

public class Biglietteria {
	private Compagnia[] compagnie = new Compagnia[2];

	public void aggiungi_compagnia(Compagnia c) {
		for (int i = 0; i < compagnie.length; i++) {
			if (compagnie[i] == null) {
				compagnie[i] = c;
				System.out.println("Compagnia aggiunta con successo");
				return;
			}
		}
		System.out.println("Compagnie al completo");
	}

	public void prenota(String codice, LinkedList<Integer> posti) {
		int count = 0;
		for (Compagnia c : compagnie) {
			for (Aereo a : c.lista_aerei) {
				if (a.getCodice().equals(codice) == true) {
					for (int p : posti) {
						a.prenota_posto(p);
						count += 1;
					}
				}
			}
		}
		if (count == 0) {
			System.out.println("Aereo non presente");
		}
	}

	public void stampa() {
		int count = 1;
		for (Compagnia c : compagnie) {
			System.out.println("Compagnia " + count + ":");
			for (Aereo a : c.lista_aerei) {
				System.out.println("Aereo " + a.getCodice() + ":");
				System.out.println("Posti: ");
				for (int i = 0; i < a.getPosti().length; i++) {
					if (a.getPosti()[i] == false) {
						System.out.print("Posto " + (i + 1) + " libero  ");
					} else {
						System.out.print("Posto " + (i + 1) + " occupato  ");
					}
				}
				System.out.println();
			}
			count += 1;
			System.out.println();
			System.out.println();
		}
	}
}
