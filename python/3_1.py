# # QUESTION 1:
# # CODE:

# def linearSearch(arr, n, x):

#     for i in range(0, n):

#         if (arr[i] == x):

#             return i
#     return -1 
# arr = [2, 4, 0, 1, 9]
# x = int(input("\nEnter element to be searched : "))
# n = len(arr)
# res = linearSearch(arr, n, x)
# if(res == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", res)



# # QUESTION 2:
# # CODE:



# def bubbleSort(arr):

#     for i in range(len(arr)):

#         for j in range(0, len(arr) - i - 1):

#             if arr[j] > arr[j + 1]:

#                 temp = arr[j]

#                 arr[j] = arr[j+1]

#                 arr[j+1] = temp

# ar = [5,8,4,3,9,1]

# bubbleSort(ar)

# print('Printing array after sorting: ')

# print(ar)

# QUESTION 3:
# CODE:

# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     while low <= high:
#         mid = (high + low)
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1
# arr = [ 2, 3, 4, 10, 40 ]
# x = int(input("\nEnter the element to be searched: "))
# result = binary_search(arr, x)
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element Not found")


# QUESTION 4:
# CODE:



def selectionSort(ar, size): 
    for i in range(size):


        low = i

        for j in range(i + 1, size):

            if ar[j] < ar[low]:

                low = j

                (ar[i], ar[low]) = (ar[low], ar[i])
arr = [4,2,3,7,8,9,1]
size = len(arr)
selectionSort(arr, size)
print('Printing array after sorting :')
print(arr)






