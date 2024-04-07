import java.util.*;

public class calculator {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int i=0;
        while(i<10)
        {
        System.out.println("Welcome in our calculator!!..");
        System.out.println("Select operator(+,-,*,/)");
        char operator = scanner.next().charAt(0);
        double result = 0;
        switch (operator) {
            case '+':
                System.out.println("Enter first input:");
                double num1 = scanner.nextDouble();
                System.out.println("Enter second input:");
                double num2 = scanner.nextDouble();
                result = num1 + num2;
                System.out.println(result);
                break;
            case '-':
                System.out.println("Enter first input:");
                double a = scanner.nextDouble();
                System.out.println("Enter second input:");
                double b = scanner.nextDouble();
                result = a - b;
                System.out.println(result);
                break;
            case '*':
                System.out.println("Enter first input:");
                double c = scanner.nextDouble();
                System.out.println("Enter second input:");
                double d = scanner.nextDouble();
                result = c * d;
                System.out.println(result);
                break;
            case '/':
                System.out.println("Enter first input:");
                double e = scanner.nextDouble();
                System.out.println("Enter second input:");
                double f = scanner.nextDouble();
                result = e / f;
                System.out.println(result);
                break;
            default:
                System.out.println("operator does not exit in our list");
                return;
        }
    }
}

}
