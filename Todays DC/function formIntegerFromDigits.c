#include <stdio.h>
#include <stdlib.h>
 
 long long int formIntegerFromDigits(char *str)
{
    long long int s=0,c=1;
    if(isdigit(str[0])) s+=str[0]-'0';
    for(int i=1;str[i]!='\0';i++){
        if(isdigit(str[i]) && str[i-1]=='-'){
            s*=10;
            s+=(str[i]-'0');
            c*=-1;
        }
        else if(isdigit(str[i])){
            s*=10;
            s+=str[i]-'0';
        }
    }
    return s*c;
}   
int main()
{
    char str[101];
    scanf("%s", str);
    printf("%lld", formIntegerFromDigits(str));
    return 0;
}