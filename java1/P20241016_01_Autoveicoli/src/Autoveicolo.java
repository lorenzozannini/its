
public class Autoveicolo {
	private int cilindarta;
	private double consumo, serbatoio;
	private String colore;
	private double prezzo;

	public Autoveicolo(int cilindarta, double consumo, double serbatoio, String colore, double prezzo) {
		super();
		this.cilindarta = cilindarta;
		this.consumo = consumo;
		this.serbatoio = serbatoio;
		this.colore = colore;
		this.prezzo = prezzo;
		
	}

	public int getCilindarta() {
		return cilindarta;
	}

	public void setCilindarta(int cilindarta) {
		this.cilindarta = cilindarta;
	}

	public double getConsumo() {
		return consumo;
	}

	public void setConsumo(double consumo) {
		this.consumo = consumo;
	}

	public double getSerbatoio() {
		return serbatoio;
	}

	public void setSerbatoio(double serbatoio) {
		this.serbatoio = serbatoio;
	}

	public String getColore() {
		return colore;
	}

	public void setColore(String colore) {
		this.colore = colore;
	}

	public double getPrezzo() {
		return prezzo;
	}

	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}

	public double CalcolaPercorrenza(int n) {
		return (double)n;
	}
}
