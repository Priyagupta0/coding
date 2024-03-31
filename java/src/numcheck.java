import java.util.*;
import java.lang.Math;

public class numcheck {
    public static void main(String[] args) {
        Scanner S = new Scanner(System.in);
        System.out.println("Enter an number:");
        double num = S.nextDouble();
        if (num == Math.floor(num)) {
            System.out.println("The given number" + num + "is an integer");
        } else {
            System.out.println("The given number" + num + "is not an integer");
        }
        S.close();
    }
}
