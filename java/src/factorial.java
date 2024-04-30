import java.util.*;
public class factorial {
    public static int CalculateFactorial(int x) {
        int fact=1;
        while(x>1){
        fact=fact*x;
        x=x-1;
        }
        return fact ;
    }

    public static void main(String args[]) {
        try (Scanner s = new Scanner(System.in)) {
            System.out.print("Enter number:");
            int num = s.nextInt();
            int fact =CalculateFactorial(num);
            System.out.print("factorial of "+num+" is : "+fact);
        }
    }
}
