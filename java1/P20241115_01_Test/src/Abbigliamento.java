
public class Abbigliamento extends Prodotto {
	
	public Abbigliamento() {
		super();
		
	}

	public Abbigliamento(String name, double price, String categoria) {
		super(name, price, categoria);
		
	}

	@Override
	public double calculateDiscount() {
		if (this.getCategoria().equals("Abbigliamento invernale")) {
			return this.getPrice() * 0.85;
		} else {
			return this.getPrice();
		}
	}
}
