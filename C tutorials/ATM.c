#include <stdio.h>
int main()
{
    int x;        //amount to be cashed
    float y = 4000.000; // amount she was left previously
    printf(" ENTER THE AMOUNT\n");
    scanf("%d", &x);
    float  z;
    if (x%5==0)
    {
        printf("processing....\n");
         if ("(x+0.5)<y")
    {
        printf("you are sufficient with amount \n", x);
        printf("the amount X is ready to get cash\n", x);
        printf("%d \n",x);
        z=y-x-0.5 ;
        printf("\n \n left balance %f",z);
    }
    else
    {
        printf("insufficeint amount\n", x);
    }
    }
    else
    {
        {
            printf("not a multiple of 5\n", x);
            printf("can't make the transcation",x);
        }
    }
   
    
    return 0;
}
