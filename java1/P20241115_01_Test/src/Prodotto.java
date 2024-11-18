
public abstract class Prodotto implements Comparable<Prodotto> {
	private String name;
	private double price;
	private String categoria;

	public Prodotto(String name, double price, String categoria) {
		super();
		this.name = name;
		this.price = price;
		this.categoria = categoria;
	}

	public Prodotto() {
		super();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	public abstract double calculateDiscount();

	@Override
	public int compareTo(Prodotto other) {
		return Double.compare(this.price, other.getPrice());
	}
	@Override
	public String toString() {
		return "Prodotto [name=" + name + ", price=" + price + ", categoria=" + categoria + "]";
	}

}
