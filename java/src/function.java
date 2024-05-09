import java.util.*;

public class function {
    public static double CalPower(int x, int y) {
        double result = Math.pow(x, y);
        return result;

    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number:");
        int a = sc.nextInt();
        System.out.print("Enter number:");
        int b = sc.nextInt();
        double result = CalPower(a, b);
        System.out.print("Result is: " + result);
    }
}