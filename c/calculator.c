#include<stdio.h>
int main(){
    int n;
    float a,b;
    printf("***MENU***\n");
    printf("1.) Addition\n 2.) Substraction\n 3.) Division\n 4.) Multiplication\n");
    printf("Choose an operation serial no. as your wish:\n");
    scanf("%d",&n);
    switch (n) {
    case 1:
    printf("enter number:");
    scanf("%f",&a);
    printf("enter number:");
    scanf("%f",&b);
   float sum=(a+b);
    printf("Addition is %f",sum);
    break;
    case 2:
    printf("enter number:");
    scanf("%f",&a);
    printf("enter number:");
    scanf("%f",&b);
   float sub =(a-b);
    printf("Subtraction is %f",sub);
    break;
    case 3:
    printf("enter number:");
    scanf("%f",&a);
    printf("enter number:");
    scanf("%f",&b);
   float mul=(a*b);
    printf("Multiplication is %f",mul);
    break;
    case 4:
    printf("enter number:");
    scanf("%f",&a);
    printf("enter number:");
    scanf("%f",&b);
  float div =(a/b);
    printf("Division is %f",div);
    break;
 default :
printf("not in listed ");
    break;
}
return 0;
}
