#include <stdio.h>
#include <stdlib.h>
 
int getProductSign(int SIZE, int arr[])
{
	int s=1;
	for(int i=0;i<SIZE;i++) s*=arr[i];
	if(s>0) return 1;
	else if(s<0) return -1;
	else return 0;
}

int main()
{
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    printf("%d", getProductSign(N, arr));
    return 0;
}