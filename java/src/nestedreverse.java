import java.util.*;

public class nestedreverse {
    public static void main(String[] args) {
        Scanner S = new Scanner(System.in);
        System.out.println("enter input:");
        int n = S.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = n; j >= i; j--) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

}
