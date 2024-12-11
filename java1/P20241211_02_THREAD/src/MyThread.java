import java.util.concurrent.locks.ReentrantLock;

public class MyThread extends Thread{
	static public long num=0;
	static public ReentrantLock mtx = new ReentrantLock();
	
	public void run() {
		mtx.lock();
		System.out.println("Ciao");
		System.out.println("Come");
		System.out.println("Va");
		for (int i=0;i<10;i++) {
			System.out.println(i);
		}
		syso
	}
}
