import java.time.LocalDateTime;

public class Volo {
	private LocalDateTime orarioImbarco;
    private LocalDateTime orarioPartenza;
    private LocalDateTime orarioArrivo;

    public Volo(LocalDateTime orarioPartenza, LocalDateTime orarioArrivo) {
    	this.orarioImbarco = orarioImbarco;
        this.orarioPartenza = orarioPartenza;
        this.orarioArrivo = orarioArrivo;
    }

	public LocalDateTime getOrarioImbarco() {
		return orarioImbarco;
	}

	public void setOrarioImbarco(LocalDateTime orarioImbarco) {
		this.orarioImbarco = orarioImbarco;
	}

	public LocalDateTime getOrarioPartenza() {
		return orarioPartenza;
	}

	public void setOrarioPartenza(LocalDateTime orarioPartenza) {
		this.orarioPartenza = orarioPartenza;
	}

	public LocalDateTime getOrarioArrivo() {
		return orarioArrivo;
	}

	public void setOrarioArrivo(LocalDateTime orarioArrivo) {
		this.orarioArrivo = orarioArrivo;
	}
}
