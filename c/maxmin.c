//finding min or max numbers
#include<stdio.h>
int minmax(int x,int y){
if(x>y) return x;
else return y;
}
int main(){
    int a,b;
        printf("enter no:");
        scanf("%d",&a);
        printf("enter no:");
        scanf("%d",&b);
        int final=minmax(a,b);
        printf("from these two numbers %d , %d , %d is larger",a,b,final);
        return 0;
}