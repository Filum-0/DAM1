import java.util.Scanner;
public class LeerDatos2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.println("Dime tu nombre: ");
        String usuario = scanner.nextLine();
        System.out.println("Hola, " + usuario );
        scanner.close();

    }
}
