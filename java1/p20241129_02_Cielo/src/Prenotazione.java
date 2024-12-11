import java.time.LocalDateTime;

public class Prenotazione {
	private LocalDateTime istante;
	private String codicePrenotazione;
	private int numeroPostiprenotati;

	public Prenotazione(LocalDateTime istante, String codicePrenotazione, int numeroPostiprenotati) {
		super();
		this.istante = istante;
		this.codicePrenotazione = codicePrenotazione;
		this.numeroPostiprenotati = numeroPostiprenotati;
	}

	public Prenotazione() {
		super();
	}

	@Override
	public String toString() {
		return "Prenotazione [istante=" + istante + ", codicePrenotazione=" + codicePrenotazione
				+ ", numeroPostiprenotati=" + numeroPostiprenotati + "]";
	}

	public LocalDateTime getIstante() {
		return istante;
	}

	public void setIstante(LocalDateTime istante) {
		this.istante = istante;
	}

	public String getCodicePrenotazione() {
		return codicePrenotazione;
	}

	public void setCodicePrenotazione(String codicePrenotazione) {
		this.codicePrenotazione = codicePrenotazione;
	}

	public int getNumeroPostiprenotati() {
		return numeroPostiprenotati;
	}

	public void setNumeroPostiprenotati(int numeroPostiprenotati) {
		this.numeroPostiprenotati = numeroPostiprenotati;
	}

}
