#include <stdio.h>
#include <stdlib.h>
 
char* stringToBits(char *str)
{
    char *s=malloc(sizeof(char)*1001);
    int si=0,x;
    for(int i=0;i<strlen(str);i++){
        x=(int)str[i]-96;
        if(x%2) s[si]='1';
        else s[si]='0';
        si++;
    }
    return s;
}

int main()
{
    char str[101];
    scanf("%s", str);
    char *bits = stringToBits(str);
    if(str == bits)
    {
        printf("New string is not formed\n");
    }
    if(bits[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", bits);
    return 0;
}