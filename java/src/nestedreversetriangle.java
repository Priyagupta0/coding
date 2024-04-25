import java.util.*;

public class nestedreversetriangle {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner S = new Scanner(System.in);
        System.out.println("enter input:");
        int n = S.nextInt();
        for (int i = 1; i <= n; i++) {
            for (int j = n; j >= i; j--) {
                System.out.print("* ");
            }
            System.out.println();
        }
        // for(int i=4;i>=1;i--){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");
        //     }
        //     System.out.print("\n");
        // }
    }

}
