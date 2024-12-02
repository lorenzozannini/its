import java.io.BufferedWriter;
import java.io.IOException;
import java.util.HashSet;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
	public static void main(String[] args) {
		HashSet<Wifi> setWifi = new HashSet<Wifi>();
		HashSet<Wifi> setWifi2 = new HashSet<Wifi>();

		while (setWifi.size() < 100) {
			setWifi.add(Wifi.buildWifi());
		}
		/*
		var write = Util.OpenFileForWriting("wifi.txt");
		for (Wifi w : setWifi) {
			try {
				write.write(
						w.getFrequenza() + ";" + w.getId() + ";" + w.getPassword() + ";" + w.getProtocollo() + "\n");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		try {
			write.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		var read = Util.OpenFileForReading("wifi.txt");
		try {
			String riga;
			String[] a = new String[4];
			while ((riga = read.readLine()) != null) {
				a = riga.split(";");
				setWifi2.add(new Wifi(Double.parseDouble(a[0]), a[1], a[2], a[3]));
			}
			read.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		for (Wifi w : setWifi2) {
			System.out.println(w);
		}
		// System.out.println(setWifi.toString());

		
		 * var write= Util.OpenFileForWriting("pippo.txt"); try { write.write("Ciao\n");
		 * write.close(); } catch (IOException e) { // TODO Auto-generated catch block
		 * e.printStackTrace(); }
		 * 
		 * var append =Util.OpenFileForAppend("pippo.txt"); try { append.write("abcd");
		 * append.close(); } catch (IOException e) { // TODO Auto-generated catch block
		 * e.printStackTrace(); }
		 * 
		 * var read =Util.OpenFileForReading("pippo.txt"); try { String riga;
		 * while((riga=read.readLine())!=null) { System.out.println(riga); }
		 * read.close(); } catch (IOException e) { // TODO Auto-generated catch block
		 * e.printStackTrace(); }
		 * 
		 * append = Util.OpenFileForAppend("pippo.txt"); int in=10; long ln=1000000000;
		 * double dn=22.0; try { append.write(in); append.write(ln); append.write(dn);
		 * 
		 * } catch (IOException e) { // TODO Auto-generated catch block
		 * e.printStackTrace(); }
		 */

		ObjectMapper objectMapper = new ObjectMapper();
		
		String jsonString = "";
		var write = Util.OpenFileForWriting("wifi.txt");
		
		for (Wifi wi:setWifi) {
			try {
				jsonString = objectMapper.writeValueAsString(wi)+"\n";
				try {
					write.write(jsonString);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			} catch (JsonProcessingException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		try {
			write.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		var read = Util.OpenFileForReading("wifi.txt");
		
		try {
			String riga;
			while ((riga = read.readLine()) != null) {
				setWifi2.add(objectMapper.readValue(riga, Wifi.class));
			}
			read.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		for (Wifi w:setWifi2) {
			System.out.println(w);
		}

	}

}
