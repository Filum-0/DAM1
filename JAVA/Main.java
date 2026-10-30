import java.util.Scanner;

public class Main {
    static Scanner sc=new Scanner(System.in);

    public static void piramideArriba(int altura) {
        for (int i = 1; i <=altura; i++)
            System.out.println(" ".repeat(altura-i) + "*".repeat(i)+"*".repeat(i-1));
    }
        public static void main(String[] args) {
            System.out.println("Dime la altura de la piramide");
            int n= Integer.valueOf(sc.nextLine());
            piramideArriba(n);
        }
}