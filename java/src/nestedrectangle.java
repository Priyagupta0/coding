
public class nestedrectangle {
    public static void main(String args[]) {
        // rectangle

        for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
        System.out.print("* ");
        }
        System.out.print("\n");
        }

        // hollow rectangle 
        System.out.print("\n");

        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 5; j++) {
                if (i == 1 || j == 1 || i == 4 || j == 5) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}