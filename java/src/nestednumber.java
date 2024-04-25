public class nestednumber {
    public static void main(String args[]) {
        // number pyramid
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
        System.out.print("\n");

        //number reverse pyramid

        for (int i = 0; i <5; i++) {
            for (int j = 1; j <= 5-i; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }

        System.out.print("\n");

        //number series pattern
         int n=1;
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(n+" ");
                n++;
            }
            System.out.println();
        }
        System.out.print("\n");

        //number pattern

        for(int i=1;i<=5;i++){
            for(int j=1;j<=i;j++){
                int sum=i+j;
                if(sum%2==0){
                    System.out.print("1"+" ");
                }
                else{
                    System.out.print("0"+" ");
                }
            }
            System.out.println();
        }
    }
}
