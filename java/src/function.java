import java.util.*;

public class function {
    public static double CalPower(int x, int y) {
        double result = Math.pow(x, y);
        return result;

    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number:");
        int a = s.nextInt();
        System.out.print("Enter number:");
        int b = s.nextInt();
        double result = CalPower(a, b);
        System.out.print("Result is: " + result);
    }
}