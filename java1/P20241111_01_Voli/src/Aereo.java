
public class Aereo {
	private boolean[] posti;
	private String codice;

	public Aereo(String codice, int posti) {
		super();
		this.codice = codice;
		this.posti = new boolean[posti];
	}

	public Aereo() {
		super();
	}

	public String getCodice() {
		return codice;
	}

	public boolean[] getPosti() {
		return posti;
	}

	public void prenota_posto(int p) {
		if (p - 1 <= posti.length) {
			if (posti[p - 1] == false) {
				posti[p - 1] = true;
				System.out.println("Posto " + p + " prenotato");
			} else {
				System.out.println("Posto " + p + " già prenotato");
			}
		} else {
			System.out.println("Posto " + p + " non esistente");
		}
	}
}
