#include <stdio.h>
#include <stdlib.h>
 
char* asciiToString(int SIZE, int *arr)
{
    char *s=malloc(sizeof(char)*SIZE+1);
    int si=0;
    for(int i=0;i<SIZE;i++){
        s[si++]=(char)arr[i];
    }
    return s;
}

int main()
{
    int N;
    scanf("%d", &N);
    int arr [N];
    for(int index = 0; index < N; index++)
    {
        scanf("%d", &arr[index]);
    }
    char *str = asciiToString(N, arr);
    if(str[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
    return 0;
}