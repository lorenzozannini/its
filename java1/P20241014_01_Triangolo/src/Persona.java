
public class Persona {
	private String nome;
	private float temperatura;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public float getTemperaturaCelsius() {
		return temperatura;
	}

	public void setTemperaturaCelsius(float temperatura) {
		this.temperatura = temperatura;
	}
	
	public float getTemperaturaFarhenheit() {
		return (float)(temperatura*9.0/5.0+32.0);
	}

	public void setTemperaturaFarhenheit(float temperatura) {
		this.temperatura = (float)(temperatura*9.0/5.0+32.0);
	}

	
}
