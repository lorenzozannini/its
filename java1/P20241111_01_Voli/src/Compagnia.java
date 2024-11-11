import java.util.LinkedList;

public class Compagnia {
	LinkedList<Aereo> lista_aerei = new LinkedList<Aereo>();

	public Compagnia() {
		super();
	}

	public void aggiungi_aereo(Aereo a) {
		lista_aerei.add(a);
		System.out.println("Aereo aggiunto con successo");
	}
}
