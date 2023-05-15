#include <stdio.h>
int fun(int n)
{
    if (n <= 1)
        return n;
    return (fun(n - 1) + fun(n - 2));
}
int countWays(int n)
{
    return fun(n + 1);
}
int main()
{
    int num;
    scanf("%d", &num);

    printf("%d", countWays(num));

    return 0;
}
