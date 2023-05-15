// #include <stdio.h>

// void traversal(int arr[],int size)
// {
//     for (int  i=0;i<size;i++) {
//         printf("%d ",arr[i]);
//     }
// }

// int binarySearch(int arr[],int size,int value)
// {
//     int low=0;
//     int high=size-1;
//     while(low<=high)
//     {
//         int mid=(low+high)/2;
//         if(arr[mid]==value)
//         {
//             return mid;
//         }
//         else if(arr[mid]<value)
//         {
//             low=mid+1;
//         }
//         else
//         {
//             high=mid-1;
//         }
//     }
//     return -1;
// }

// int main()
// {
//    int arr[100]={5, 7, 9, 11, 15, 20, 30, 45, 89, 97};
//    int size=10;
//    int element,search;
//    printf("Enter the element you want to search:-\n");
//    scanf("%d",&element);
   
  
//    search=binarySearch(arr,size,element);
//    printf("\n");
//    if(search == -1)
//    {
//         printf("Search element not found.\n");
//    }
//    else
//    {
      
//        printf("The element is found at %d position\n",search);
//    }
   

//     return 0;
// }


#include <stdio.h>

void printArray(int *A, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}
void bubbleSort(int *A, int n)
{
    int temp;
    int isSorted = 0;
    int i, j;
    for (i = 0; i < n - 1; i++) // For number of pass
    {
        for (j = 0; j < n - 1 - i; j++) // For comparison in each pass
        {
            if (A[j] > A[j + 1])
            {
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
        printf("After Pass %d --> ",i+1);
        for(int i=0;i<n;i++)
        {
            printf("%d ",A[i]);
        }
        printf("\n");
    }

}



int main()
{
    int size;
    int A[100];
    printf("Enter size of the array :-\n");
    scanf("%d", &size);
    printf("Enter elements in array :-\n");
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &A[i]);
    }

    bubbleSort(A, size); // Function to sort the array

    printf("After sorting :-\n");

    printArray(A, size); // Printing the array before sorting
    return 0;
}
