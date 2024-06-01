#include<stdio.h>
int factorial(int x){
    int output,n;
    printf("enter number:");
    scanf("%d",&n);
    if(n==0)
    printf("Not Possible");
else if (n==1)
printf("factorial of %d is 1",n);
else {
     output =  x * factorial(x-1);
}
    return output;
}
int main(){
    int result = factorial(n);
    printf("the factorial of %d is %d",n,result);
return 0;
}