#include <stdio.h>
#include <stdlib.h>
 
void printSamePositionDigitsSum(int num1, int num2)
{
    int a[1001],ai=0;
    while(num1 && num2){
        a[ai++]=num1%10+num2%10;
        num1/=10;
        num2/=10;
    }
    if(num1) a[ai++]=num1;
    else if(num2) a[ai++]=num2;
    int x=ai;
    for(int i=x-1;i>=0;i--) printf("%d",a[i]);
}

int main()
{
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printSamePositionDigitsSum(num1, num2);
    return 0;
}