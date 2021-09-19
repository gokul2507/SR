#include <stdio.h>
#include <stdlib.h>
 
int* addDigit(int *arr, int SIZE, int D)
{
}
int main()
{
    int N, digit;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    scanf("%d", &digit);
    int *ptr = addDigit(arr, N, digit);
    int index = 0;
    while(*(ptr+index) != -1)
    {
        printf("%d ", ptr[index]);
        index++;
    }
    return 0;
}