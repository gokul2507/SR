#include <stdio.h>
#include <stdlib.h>
 
char* getAbbreviation(char *str)
{
    int si=0;
    char *s=malloc(sizeof(char)*1001);
    char *t=strtok(str," ");
    while(t!=NULL){
        s[si++]=toupper(t[0]);
        t=strtok(NULL," ");
    }
    return s;
}

int main()
{
    char str[1001];
    scanf("%[^\n]", str);
    char *abbreviation = getAbbreviation(str);
    if(abbreviation == str)
    {
        printf("New string is not formed\n");
    }
    if(abbreviation[0] == '\0')
    {
        printf("String is empty");
    }
    printf("%s", abbreviation);
    return 0;
}