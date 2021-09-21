#include <stdio.h>
#include <stdlib.h>
 
char* hexCodeToString(char *hexCode)
{
    char *s=malloc(sizeof(char)*10001);
    int si=0;
    char *t=strtok(hexCode," ");
    while(t!=NULL){
        s[si++]=(char)strtol(t,NULL,16);
        t=strtok(NULL," ");
    }
    s[si]='\0';
    return s;
}

int main()
{
    char hexCode[1001];
    scanf("%[^\n]", hexCode);
    char *str = hexCodeToString(hexCode);
    if(str == hexCode)
    {
        printf("New string is not formed\n");
    }
    if(str[0] == '\0')
    {
        printf("String is empty\n");
    }
    printf("%s", str);
}

