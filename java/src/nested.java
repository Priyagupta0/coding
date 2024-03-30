import java.util.Scanner;

public class nested {
    public static void main(String[] args) {
        System.out.println("Enter input:");
        double num = Scanner.nextDouble();
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                System.out.println(" * ");
            }
            System.out.println();
        }
    }

}
