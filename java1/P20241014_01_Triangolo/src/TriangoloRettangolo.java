
public class TriangoloRettangolo {
	
	private void RicalcolaIpotenusa() {
		ipot = Math.sqrt(cat1 * cat1 + cat2 * cat2);
	}

	private double cat1, cat2, ipot;

	public double getCat1() {
		return cat1;
	}

	public void setCat1(double cat1) {
		this.cat1 = cat1;
		RicalcolaIpotenusa();
	}

	public double getCat2() {
		return cat2;
	}

	public void setCat2(double cat2) {
		this.cat2 = cat2;
		RicalcolaIpotenusa();
	}

	public double getIpot() {
		return ipot;
	}

	public TriangoloRettangolo(double cat1, double cat2) {
		super();
		this.cat1 = cat1;
		this.cat2 = cat2;
		RicalcolaIpotenusa();
	}

	double Area() {
		return cat1 * cat2 / 2.0;
	}

	double Perimetro() {
		return cat1 + cat2 + ipot;
	}

}
