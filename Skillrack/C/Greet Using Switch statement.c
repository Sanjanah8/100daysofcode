#include<stdio.h>
#include<stdlib.h>

int main()
{
char ch;
scanf("%c",&ch);
switch(toupper(ch)){
    case 'M':
    printf("Good Morning!");
    return 0;
    case 'E':
    printf("Good Evening!");
    return 0;
    case 'N':
    printf("Good Night");
    return 0;
}
}
