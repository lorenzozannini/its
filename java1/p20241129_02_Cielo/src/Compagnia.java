
public class Compagnia {

	private String nomeCompagnia;

	public String getNomeCompagnia() {
		return nomeCompagnia;
	}

	public void setNomeCompagnia(String nomeCompagnia) {
		this.nomeCompagnia = nomeCompagnia;
	}

	public Compagnia() {
		super();
	}

	public Compagnia(String nomeCompagnia) {
		super();
		this.nomeCompagnia = nomeCompagnia;
	}

	@Override
	public String toString() {
		return "Compagnia [nomeCompagnia=" + nomeCompagnia + "]";
	}

}
