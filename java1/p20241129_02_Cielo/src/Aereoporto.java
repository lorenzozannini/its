
public class Aereoporto {

	private String codiceAereoporto;
	private String citta;

	public String getCodiceAereoporto() {
		return codiceAereoporto;
	}

	public void setCodiceAereoporto(String codiceAereoporto) {
		this.codiceAereoporto = codiceAereoporto;
	}

	public String getCitta() {
		return citta;
	}

	public void setCitta(String citta) {
		this.citta = citta;
	}

	public Aereoporto() {
		super();
	}

	public Aereoporto(String codiceAereoporto, String citta) {
		super();
		this.codiceAereoporto = codiceAereoporto;
		this.citta = citta;
	}

	@Override
	public String toString() {
		return "Aereoporto [codiceAereoporto=" + codiceAereoporto + ", citta=" + citta + "]";
	}

}
