
public class Aereo {
	private String codiceAereo;
	private int numeroPosti;

	public Aereo(String codiceAereo, int numeroPosti) {
		super();
		this.codiceAereo = codiceAereo;
		this.numeroPosti = numeroPosti;
	}

	public Aereo() {
		super();
	}

	@Override
	public String toString() {
		return "Aereo [codiceAereo=" + codiceAereo + ", numeroPosti=" + numeroPosti + "]";
	}

	public String getCodiceAereo() {
		return codiceAereo;
	}

	public void setCodiceAereo(String codiceAereo) {
		this.codiceAereo = codiceAereo;
	}

	public int getNumeroPosti() {
		return numeroPosti;
	}

	public void setNumeroPosti(int numeroPosti) {
		this.numeroPosti = numeroPosti;
	}

}
