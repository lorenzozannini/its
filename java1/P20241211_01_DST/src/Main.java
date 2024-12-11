import java.util.*;

public class Main {

	public static void main(String[] args) {
		
		Queue<Integer> qi = new LinkedList<Integer>();
		qi.add(9);
		qi.add(8);
		qi.add(11);
		qi.add(3);
		System.out.println(qi);
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		System.out.println(qi.poll());
		
		Stack<Integer> si= new Stack<Integer>();
		si.push(100);
		si.push(110);
		si.push(20);
		si.push(30);
		System.out.println(si.pop());
		
	}

}
