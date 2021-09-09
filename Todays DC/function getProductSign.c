#include <stdio.h>
#include <stdlib.h>
 
int getProductSign(int SIZE, int arr[])
{
	int s=arr[0];
	for(int i=1;i<SIZE;i++){
	    if(arr[i]>0) s*=1;
	    else if(arr[i]<0) s*=-1;
	    else{
	        return 0;
	    }
	}
	if(s>0) return 1;
	else return -1;
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