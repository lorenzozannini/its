import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class ProductManager implements Ordinabile {
	private List<Prodotto> products = new LinkedList<Prodotto>();

	public ProductManager(List<Prodotto> products) {
		super();
		this.products = products;
	}

	public ProductManager() {
		super();
	}

	public List<Prodotto> getProducts() {
		return products;
	}

	public void setProducts(List<Prodotto> products) {
		this.products = products;
	}

	public void addProduct(Prodotto p) {
		products.add(p);
	}

	@Override
	public List<Prodotto> sortByPrice(List<Prodotto> products) {
		Collections.sort(products, new Comparator<Prodotto>() {
			@Override
			public int compare(Prodotto p1,Prodotto p2) {
				return p1.compareTo(p2);
			}
		});
		return products;
	
	}
	
	public void displayProduts() {
		System.out.println("Lista prodotti:");
		for (Prodotto p : products) {
			System.out.println(p.toString());
		}
		System.out.println();
	}
	
	public void displaySortedProduts() {
		System.out.println("Lista prodotti in ordine crescente:");
		for (Prodotto p:this.sortByPrice(products)) {
			System.out.println(p.toString());
		}
		System.out.println();
	}
}
