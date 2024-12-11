
public class Agenzia {

	private String nomeAgenzia;

	public String getNomeAgenzia() {
		return nomeAgenzia;
	}

	public void setNomeAgenzia(String nomeAgenzia) {
		this.nomeAgenzia = nomeAgenzia;
	}

	public Agenzia() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Agenzia(String nomeAgenzia) {
		super();
		this.nomeAgenzia = nomeAgenzia;
	}

	@Override
	public String toString() {
		return "Agenzia [nomeAgenzia=" + nomeAgenzia + "]";
	}

}
