
import java.util.Scanner;
public class NumeroPositivoNegativo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Dime un numero entero: ");
        int numero = scanner.nextInt();

        if (numero>=1){
            System.out.println(numero + "Positivo");
        }else if (numero < 0) {
            System.out.println(numero + " Negativo");
        }else{
            System.out.println("es zero");

        }

    }
}
