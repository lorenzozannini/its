import java.util.*;

public class Main {
	
	static public Queue<Integer> q = new LinkedList<Integer>();
	
	public static void main(String[] args) {
		Produttore p = new Produttore();
		Consumatore c = new Consumatore();
		
		p.start();
		c.start();
		
		
	}

}
