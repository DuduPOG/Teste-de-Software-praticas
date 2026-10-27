import java.util.Scanner;

public class Triangulo {

    public static String classificarTriangulo(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return "Lados invalidos";
        }
        if (a + b <= c || a + c <= b || b + c <= a) {
            return "Nao eh um triangulo";
        }
        if (a == b && b == c) {
            return "Equilatero";
        } else if (a == b || b == c || a == c) {
            return "Isosceles";
        } else {
            return "Escaleno";
        }
    }

    public static void main(String[] args) {
        
        System.out.println("Digite 3 lados de um triângulo para verificar qual é seu tipo:");
        System.out.println("Tipos possíveis: Equilátero, Isósceles e Escaleno");
    
       int a, b, c;
       
       Scanner sc = new Scanner(System.in);

       a = sc.nextInt();
       b = sc.nextInt();
       c = sc.nextInt();
    
       System.out.println(Triangulo.classificarTriangulo(a, b, c));

       sc.close();
    }

}