#include<stdio.h>
int main()
{
    /* code */
    float km,cm,miles,kg,pounds;
        printf("pick any of the conversion :\n");
        printf("km to miles:\n");
        printf("cm to miles:\n");    
        printf("pounds to kg:\n");
        int a;
        scanf("%d",&a);
        switch(a)
        {
            case 1:
            printf("\n enter the value in KM ");
            scanf("%f", &km);
            miles=km*0.62;
            printf("\n In miles it is %f",miles);
            break;

             case 2:
            printf("\n enter the value in CM ");
            scanf("%f", &cm);
            miles=cm*100000*0.62;
            printf("\n In miles it is %f",miles);
            break;

             case 3:
            printf("\n enter the value in POUNDS");
            scanf("%f", &pounds);
            kg=pounds*0.453592;
            printf("\n In KG it is %f",kg);
            break;
             
        }

     printf(" \n hope you get the required answer ")   ;
    return 0;
}


