# 171044098
# Akif Kartal
# Q4 Real Code
import random

number_of_swap = 0
def main():
    global number_of_swap
    print("Quick Sort")
    arr = [57, 19, 46, 50, 4, 41, 43, 56, 37, 28, 17, 45, 7, 34, 10, 45, 40, 55, 14, 68]
    print("-----------------------------------------------------------------------")
    print("Array before sorting: ", arr)
    number_of_swap = 0
    print("Number of Swap before sorting: ", number_of_swap)
    quicksort(arr,0,len(arr)-1)
    print("-----------------------------------------------------------------------")
    print("Array after sorting: ", arr)
    print("Number of Swap after sorting: ", number_of_swap)
    print("-----------------------------------------------------------------------")
    print("Insertion Sort")
    arr = [57, 19, 46, 50, 4, 41, 43, 56, 37, 28, 17, 45, 7, 34, 10, 45, 40, 55, 14, 68]
    print("-----------------------------------------------------------------------")
    print("Array before sorting: ", arr)
    number_of_swap = 0
    print("Number of Swap before sorting: ", number_of_swap)
    insertionsort(arr, len(arr))
    print("-----------------------------------------------------------------------")
    print("Array after sorting: ", arr)
    print("Number of Swap after sorting: ", number_of_swap)

def quicksort(A, l, h):

    if h > l:
        p = partition(A, l, h)
        quicksort(A, l, p - 1)
        quicksort(A, p + 1, h)
def insertionsort(A,n):
    global number_of_swap
    for i in range(1,n):
        current = A[i]
        pos = i-1
        while (pos >= 0) and (current < A[pos]):
            number_of_swap = number_of_swap + 1
            A[pos+1] = A[pos]
            pos = pos - 1
        number_of_swap = number_of_swap + 1
        A[pos + 1] = current
def partition(A, l, h):
    global number_of_swap
    pivot = A[h]
    i = l
    for j in range(l, h):
        if A[j] < pivot:
            number_of_swap = number_of_swap + 1
            A[i], A[j] = A[j], A[i]
            i = i + 1
    number_of_swap = number_of_swap+1
    A[i], A[h] = A[h], A[i]
    return i

main()
