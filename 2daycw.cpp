
// WEDNESDAY
// #include <iostream>
// #include <algorithm>
// using namespace std;
// int main()
// {
//     int n;
//     cout << "Enter the size of an array" << endl;
//     ;

//     cin >> n;
//     int a[n];
//     cout << "Enter the unsorted  array" << endl;
//     for (int i = 0; i < n; i++)
//     {
//         cin >> a[i];
//     }
//     cout<<endl;
//     cout<<endl;
//     int counter = 1;
//     while (counter < n)
//     {
//         for (int i = 0; i < (n - counter); i++)
//         {
//             if (a[i] > a[i + 1])
//             {
//                 int temp = a[i];
//                 a[i] = a[i + 1];
//                 a[i + 1] = temp;
//                 cout<<"Sorting steps"<<endl;
//                 for (int i = 0; i < n; i++)
//                 {
//                     cout << a[i] << "       ";
//                 }cout<<endl;
//             }
//         }
//         counter++;

//         cout << endl;
//     }
//      cout<<endl;
//     cout<<endl;
//     cout << "SORTED ARRAY " << endl;
//     for (int i = 0; i < n; i++)
//     {
//         cout << a[i] << "       ";
//     }
//     return 0;
// }

// FRIDAY
#include <iostream>
#include <algorithm>
using namespace std;
void swap(int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
int partition( int arr[], int l ,int r)
{
    int pivot = arr[r];
    int i = l - 1;
    for (int j = arr[l]; j < r; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, r);
    return i + 1;
}
void quicksort(int arr[], int l, int r)
{
    if (l < r)
    {
        int pi = partition(arr, l, r);
        quicksort(arr, l, pi - 1);
        quicksort(arr, l, pi + 1);
    }
}
    int main()
    {
        int n;
        cout << "Enter the size of an array" << endl;

        cin >> n;
        int arr[n];
        cout << "Enter the unsorted  array" << endl;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        cout << endl;
        quicksort(arr, 0, n - 1);
        cout << "SORTED ARRAY " << endl;
        for (int i = 0; i < n; i++)
        {
            cout << arr[i] << "       ";
        }
        return 0;
    }
