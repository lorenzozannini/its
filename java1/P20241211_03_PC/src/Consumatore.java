import java.util.Random;

public class Consumatore extends Thread {

	public void run() {
		int somma = 0;
		int nEl = 0;
		int tot = 0;
		Random rng = new Random();
		while (true) {
			int sleep = rng.nextInt(100, 500);
			tot += sleep;
			while (!Main.q.isEmpty()) {
				int n = Main.q.poll();
				somma+=n;
				nEl+=1;
			}
			if (tot>=2000) {
				tot=0;
				System.out.println("Somma "+somma);
				System.out.println("Media "+ (somma/nEl));
			}
			try {
				Thread.sleep(sleep);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
