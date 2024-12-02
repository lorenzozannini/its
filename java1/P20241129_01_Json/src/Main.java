import java.util.LinkedList;
import java.util.Locale;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {

	public static void main(String[] args) throws JsonProcessingException {
		// Locale.setDefault(Locale.US);
		Persona p1 = new Persona(1L, "iris", false, 45000.0);
		ObjectMapper objectMapper = new ObjectMapper();
		String jsonp = """
				{"id":1,"nome":"iris","femmina":false,"stipendio":45000.0}
				""";

		System.out.println(p1.SerializeJson());
		System.out.println(p1.DeserializeJson(p1.SerializeJson()));
		LinkedList<Persona> lp = new LinkedList<Persona>();
		lp.add(p1);
		lp.add(new Persona(2L, "Aldo", true, 90000.0));
		lp.add(new Persona(3L, "Ardarello", false, 80000.0));
		String slp = objectMapper.writeValueAsString(lp);
		System.out.println(slp);
		
		var lp1=objectMapper.readValue(slp,new LinkedList<Persona>().getClass());
		System.out.println(lp1);
	}

}
