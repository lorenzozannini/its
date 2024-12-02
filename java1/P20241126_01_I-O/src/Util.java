import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.Random;

public class Util {
	private static Random rng = new Random();
	private static String alfabeto = "abcdefghijklmnopqrstuvwxyz";
	private static String digit = "0123456789";
	private static String simboli = "-_.:,!?|$%";

	public static String GetRandomAuthProto() {
		int rInt = rng.nextInt(4);
		switch (rInt) {
		case 0: {

			return "WEP";
		}
		case 1: {

			return "WPA";
		}
		case 2: {

			return "WPA2";
		}
		case 3: {

			return "WPA3";
		}
		default: {
			return null;
		}
		}
	}

	public static Double GetFrequenza() {
		Double k = rng.nextDouble(1000000000.0, 5000000000.0);
		return k;
	}

	public static String GetPassword(Boolean isPassword) {
		String all = alfabeto + alfabeto.toUpperCase() + digit;
		if (isPassword) {
			all += simboli;
		}
		int rIndex = rng.nextInt(12, 25);
		String pass = "";
		for (int i = 0; i < rIndex; i++) {
			pass += all.charAt(rng.nextInt(all.length()));
		}
		return pass;
	}

	public static BufferedWriter OpenFileForWriting(String nomeFile) {
		try {
			Path path = Path.of(nomeFile);
			BufferedWriter writer = Files.newBufferedWriter(path,
					Files.exists(path) ? StandardOpenOption.TRUNCATE_EXISTING : StandardOpenOption.CREATE);
			return writer;
		} catch (Exception ex) {
			return null;
		}
	}

	public static BufferedReader OpenFileForReading(String nomeFile) {

		try {
			BufferedReader reader = Files.newBufferedReader(Path.of(nomeFile));
			return reader;
		} catch (IOException e) {
			return null;
		}
	}
}