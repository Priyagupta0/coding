//adding numbers
#include<stdio.h>
int add(int x,int y){
  int result=(x+y);
  return result;
}
int main(){
    int a,b;
printf("Enter number :");
scanf("%d",&a);
printf("Enter number :");
scanf("%d",&b);
int sum = add(a,b);
printf("result of adding two numbers %d,%d is %d",a,b,sum);
return 0;
}
