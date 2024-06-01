#include<stdio.h>

void swap(int *xp, int *yp){
    int temp=*xp;
    *xp=*yp;
    *yp=temp;
}
    
void selectionsort(int arr[],int n){
    int minindex;
    for(int i=0;i<n-1;i++){
        int minindex=i;
    for(int j=0;j<n-i-1;j++){
    if(arr[j]<arr[minindex]){
    minindex=j;
    }
}
 swap(&arr[minindex],&arr[i]);
}
}
int main(){
    int n;
    printf("Enter size of an array:");
    scanf("%d",&n);
    int arr[n];
    printf("Element of an array:\n");
    for(int i=0;i<n;i++){
    scanf("%d",&arr[i]);
    }
    selectionsort(arr,n);

    printf("Sorted array:\n");
    for(int i=0;i<n;i++){
        printf("%d",arr[i]);
        printf("\n");
    }
    return 0;
}


 
