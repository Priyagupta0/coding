import java.util.*;
public class Percentcalc {    
    public static void main( String[] args){
     @SuppressWarnings("resource")
        Scanner S = new Scanner(System.in);
        System.out.println("enter the marks of first subject :");
        double sub1 = S.nextDouble();
        System.out.println("enter the marks of second subject :");
        double sub2 = S.nextDouble();
        System.out.println("enter the marks of third subject :");
        double sub3 = S.nextDouble();
        System.out.println("enter the marks of fourth subject :");
        double sub4 = S.nextDouble();
        System.out.println("enter the marks of fivth subject :");
        double sub5 = S.nextDouble();
        double result = (((sub1 + sub2 + sub3 + sub4 + sub5)/500)*100);
        System.out.println("Result is " + result + "%");
    }
}

