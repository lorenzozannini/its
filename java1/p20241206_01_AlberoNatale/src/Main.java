import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int space = 1;
		Scanner input = new Scanner(System.in);
		System.out.print("Altezza albero di Natale( maggiore di 1)->");
		int len = (input.nextInt())+1;
		System.out.println(" ".repeat(len) + "/" + "\\");
		len -= 1;
		int i=1;
		while (len >= 0) {
			if (i % 2 == 0) {
				System.out.println(" ".repeat(len) + "/" + " ".repeat(space * 2) + "\\");
				space += 1;
				
			} else {
				System.out.println(" ".repeat(len) + "/" + "_" + " ".repeat((space * 2) - 2) + "_" + "\\");
				len -= 1;
			}
			i+=1;
		}
	}

}
