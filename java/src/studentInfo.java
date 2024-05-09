import java.util.*;

public class studentInfo {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number of students:");
        int n = s.nextInt();
        String[] name = new String[n];
        double[] marks = new double[n];
        for (int i = 0; i < n; i++) {
            System.out.println("Enter student name:");
            name[i] = s.next();
            System.out.println("Enter student total marks:");
            marks[i] = s.nextDouble();
        }
        System.out.println("Student Information:");
        System.out.println("Name" + " : " + "Marks");
        for (int i = 0; i < n; i++) {
            System.out.println(name[i] + " : " + marks[i]);
        }
    }
}