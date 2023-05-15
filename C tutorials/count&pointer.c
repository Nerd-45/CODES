#include<stdio.h>
int main()
{
    /* code */
    char a[20];
        printf("enter the name word by word \n");
     gets(a);
     int c= strlen(a);
     int *p= &c;
     printf("the count  is %d ",*p);
     
    return 0;
}




