#include<stdio.h>
int add(int x,int y){
  int result;
  result=(x+y);
}
int main(){
    int a,b,result;
printf("Enter number :");
scanf("%d",&a);
printf("Enter number :");
scanf("%d",&b);
add(a,b);
printf("result of adding two numbers %d,%d is %d",a,b,result);
}