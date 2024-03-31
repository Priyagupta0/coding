import java.util.*;
import java.lang.Math;

public class quadraticroots {
    public static void main (String[] args){
//finding roots of the given equation coefficient
Scanner scanner = new Scanner(System.in);
System.out.println("enter first coefficient:");
double num1 = scanner.nextDouble();
System.out.println("enter second coefficient:");
double num2 = scanner.nextDouble();
System.out.println("enter third coefficient:");
double num3 = scanner.nextDouble();
System.out.println("The roots are - \n");
double root1 = ((-(num2) + Math.sqrt(((num2)*(num2)) - (4*num1*num3)))/(2*(num1)));
double root2 = ((-(num2) - Math.sqrt(((num2)*(num2)) - (4*num1*num3)))/(2*(num1)));
System.out.println(root1);
System.out.println(root2);
}
}
