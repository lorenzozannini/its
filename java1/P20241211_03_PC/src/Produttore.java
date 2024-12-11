import java.util.Random;

public class Produttore extends Thread {

	public void run() {
		Random rng = new Random();
		while (true) {
			int n = rng.nextInt(0, 100);
			int sleep = rng.nextInt(100, 1000);
			Main.q.add(n);
			try {
				Thread.sleep(sleep);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
