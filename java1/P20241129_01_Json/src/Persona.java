import java.util.HashSet;
import java.util.Random;
import java.util.Set;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Persona {
	private Long id;
	private String nome;
	private Boolean femmina;
	private Double stipendio;

	public Set<Integer> numeri;

	public Persona(Long id, String nome, Boolean femmina, Double stipendio) {
		super();
		this.id = id;
		this.nome = nome;
		this.femmina = femmina;
		this.stipendio = stipendio;
		numeri = new HashSet<Integer>();
		Random rng= new Random();
		numeri.add(rng.nextInt());
		numeri.add(rng.nextInt());
		numeri.add(rng.nextInt());
	}

	public Persona() {
		super();
	}

	@Override
	public String toString() {
		return "Persona [id=" + id + ", nome=" + nome + ", femmina=" + femmina + ", stipendio=" + stipendio
				+ ", numeri=" + numeri + "]";
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public Boolean getFemmina() {
		return femmina;
	}

	public void setFemmina(Boolean femmina) {
		this.femmina = femmina;
	}

	public Double getStipendio() {
		return stipendio;
	}

	public void setStipendio(Double stipendio) {
		this.stipendio = stipendio;
	}

	public String SerializeJson() {
		ObjectMapper objectMapper = new ObjectMapper();
		String ret = "";
		try {
			ret = objectMapper.writeValueAsString(this);
		} catch (JsonProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return ret;
		// return
		// String.format("{\"id\":%d,\"nome\":%s,\"femmina\":%b,\"stipendio\":%.2f}",id,nome,
		// femmina, stipendio);
	}

	public Persona DeserializeJson(String s) {
		ObjectMapper objectMapper = new ObjectMapper();
		Persona p;
		try {
			p = objectMapper.readValue(s, Persona.class);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
			p = null;
		}
		return p;
	}

}
