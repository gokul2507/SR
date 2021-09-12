#include <stdio.h>
#include <stdlib.h>
 
int countDigitsInWords(char *str)
{
    int a[128]={0},c=0;
    for(int i=0;str[i]!='\0';i++) a[tolower(str[i])]+=1;
    if(a['z']&&a['e']&&a['r']&&a['o']) c+=1;
    if(a['o']&&a['n']&&a['e']) c+=1;
    if(a['t']&&a['w']&&a['o']) c+=1;
    if(a['t']&&a['h']&&a['r']&&a['e']>1) c+=1;
    if(a['f']&&a['o']&&a['u']&&a['r']) c+=1;
    if(a['f']&&a['i']&&a['v']&&a['e']) c+=1;
    if(a['s']&& a['i']&&a['x']) c+=1;
    if(a['s']&&a['e']>1&&a['v']&&a['n']) c+=1;
    if(a['e']&&a['i']&&a['g']&&a['h']&&a['t']) c+=1;
    if(a['n']>1&&a['i']&&a['e']) c+=1;
    return c;
        
}

int main()
{
    char str[101];
    scanf("%[^\n\r]", str);
    printf("%d", countDigitsInWords(str));
    return 0;
}