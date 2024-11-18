
public class ProductApp {

	public static void main(String[] args) {
		ProductManager productManager1= new ProductManager();
		productManager1.addProduct(new Elettronica("Laptop", 1200.00, "Pc"));
		productManager1.addProduct(new Abbigliamento("Maglione", 50.00, "Abbigliamento invernale"));
		productManager1.addProduct(new Elettronica("Smartphone", 800.00, "Elettronica"));
		productManager1.addProduct(new Abbigliamento("T-shirt", 20.00, "Abbigliamento estivo"));
		productManager1.addProduct(new Elettronica("Cuffie Bluetooth", 150.00, "Accessorio"));
		productManager1.displayProduts();
		productManager1.displaySortedProduts();
		
	}

}
