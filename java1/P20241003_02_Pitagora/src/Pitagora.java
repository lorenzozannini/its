
public class Pitagora {

	public static void main(String[] args) {
		double c1 = 10.345, c2 = 20.415, ipotenusa, perimetro, area;

		ipotenusa = Math.sqrt((c1 * c1) + (c2 * c2));
		perimetro = c1 + c2 + ipotenusa;
		area = (c1 * c2) / 2;
		
		System.out.println("1) La lunghezza dell'ipotenusa vale: " + ipotenusa);
		System.out.println("2) Il perimetro del triangolo rettangolo vale: " + perimetro);
		System.out.println("3) L'area del triangolo rettangolo vale: " + area);

	}

}
