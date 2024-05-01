class A{
    public void setValue(int x){
        int value = x;
    }
    public int getValue(int value){
        return ++value;
    }
}
public class practice {
    public static void main(String args[]){
        A r = new A();
        int result = r.getValue(100);
        System.out.print(result);
    }
}
