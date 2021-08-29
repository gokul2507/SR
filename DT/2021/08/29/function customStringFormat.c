#include <stdio.h>
#include <stdlib.h>
 
void customStringFormat(char *str1, char *str2)
{
}

int main()
{
    char str1[10001], str2[10001];
    scanf("%[^\n]\n%[^\n]", str1, str2);
    customStringFormat(str1, str2);
    return 0;
}