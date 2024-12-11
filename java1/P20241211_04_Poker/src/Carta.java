import java.util.Random;

public class Carta {
	private String[] semi = { "Cuori", "Quadri", "Fiori", "Picche" };
	private String[] numeri = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" };
	private String seme;
	private String numero;

	public Carta() {
		super();
		Random rng = new Random();
		numero = numeri[rng.nextInt(0, 13)];
		seme = semi[rng.nextInt(0, 4)];
	}

	public String getSeme() {
		return seme;
	}

	public String getNumero() {
		return numero;
	}

	@Override
	public String toString() {
		return "Carta [seme=" + seme + ", numero=" + numero + "]";
	}

}
