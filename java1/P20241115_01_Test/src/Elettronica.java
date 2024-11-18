
public class Elettronica extends Prodotto {

	public Elettronica() {
		super();

	}

	public Elettronica(String name, double price, String categoria) {
		super(name, price, categoria);

	}

	@Override
	public double calculateDiscount() {
		if (this.getPrice() > 500.0) {
			return this.getPrice() * 0.90;
		} else {
			return this.getPrice();
		}
	}
}
