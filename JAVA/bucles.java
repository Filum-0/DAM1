
import java.util.Scanner;

public class bucles {
    public static void main(String[] args) {


        int contador = 0;

        while (contador < 5) {
            System.out.println("Contando: " + contador);
            contador++; // ¡Importante! Si olvidas esto, tendrás un bucle infinito
        }



        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("1. Jugar");
            System.out.println("0. Salir");
            opcion = sc.nextInt();
        } while (opcion != 0);

        System.out.println("Fin del juego");

//    Inicio  ;  Condición ; Paso
        for (int i = 1; i < 50; i++) {
            System.out.println("Iteración número " + i);
        }

        String[] nombres = {"Ana", "Luis", "Pedro"};

// Versión Clásica (Propensa a errores de índice)
        for (int i = 0; i < nombres.length; i++) {
            System.out.println(nombres[i]);
        }

// Versión For-Each (Limpia y segura)
        for (String nombre : nombres) {
            System.out.println(nombre);
        }

        for (int i = 0; i < 1000; i++) {
            System.out.println(i);
            if (i == 5) {
                System.out.println("Encontrado el 5. ¡Me voy!");
                break; // Sale del bucle, no llega a 1000

            }
        }



    }
}
