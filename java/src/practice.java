import java.util.*;

public class practice {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of students:");
        int n = sc.nextInt();
        String[] name = new String[n];
        double[] marks = new double[n];
        for (int i = 0; i < n; i++) {
            System.out.println("Enter student name:");
            name[i] = sc.next();
            System.out.println("Enter student total marks:");
            marks[i] = sc.nextDouble();
        }
        System.out.println("Student Information:");
            System.out.print(name);
            System.out.println(marks);
    }
}