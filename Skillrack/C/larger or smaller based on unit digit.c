#include<stdio.h>
#include<stdlib.h>

int main()
{
int n1,n2;
scanf("%d %d",&n1,&n2);
if((n1%10)==(n2%10)){
    if(n1<n2){
        printf("%d",n2);
    }
    else{
        printf("%d",n1);
    }
}
else if(n1>n2){
    printf("%d",n2);
}
else{
    printf("%d",n1);
}return 0;
}
