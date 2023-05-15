#include <stdio.h>
 

int totalWays(int n)
{
    
    if (n < 0) {
        return 0;
    }
 
    
    if (n == 0) {
        return 1;
    }
 
    
    return totalWays(n - 1) + totalWays(n - 2) ;
}
 
int main(void)
{
    int n ;
    scanf("%d",&n);
    printf("Total ways to reach the %d'th stair are %d", n, totalWays(n));
 
    return 0;
}




