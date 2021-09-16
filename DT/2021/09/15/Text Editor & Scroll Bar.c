#include<stdio.h>
#include<stdlib.h>

int main()
{
    int X,Y;
    scanf("%d %d\n",&X,&Y);
    long long int totalLines=0,currLineChar=0;
    char word[101];
    while(scanf("%s ",word)==1){
        int len=strlen(word);
        if(len+currLineChar<=Y){
            currLineChar+=len;
            currLineChar++;
        }
        else{
            totalLines++;
            currLineChar=len+1;
        }
    }
    totalLines++;
    if(totalLines<=X){
        printf("0");
    }
    else{
        printf("%lld",totalLines-X);
    }
}