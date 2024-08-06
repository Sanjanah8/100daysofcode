#include<stdio.h>
<include<limits.h>
int main()
{
unsigned long long int n;
scanf("%llu",&n);
if(n<=INT_MAX)
{
printf("I");
}
else{
printf("L");
}
return 0;
}
