# 171044098
# Akif Kartal
# Q3 Real Code
import random


def main():
    arr = [random.randint(1, 1000) for _ in range(100)] #create random array with size 100
    print("-----------------------------------------------------------------------")
    print("Array before sorting: ", arr)
    quicksort_improved(arr, 0, len(arr)-1)
    print("-----------------------------------------------------------------------")
    print("Array after sorting: ", arr)


def quicksort_improved(A, l, h):
    if l < h:
        if (h-l) < 25:
            insertionsort(A, l, h+1)
        else:
            p = partition(A, l, h)
            quicksort_improved(A, l, p-1)
            quicksort_improved(A, p+1, h)


def insertionsort(A, l, h):
    for i in range(l+1, h):
        current = A[i]
        pos = i-1
        while (pos >= 0) and (current < A[pos]):
            A[pos+1] = A[pos]
            pos = pos - 1
        A[pos + 1] = current


def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while (i < j):
        while (A[i] <= pivot):
            i = i+1
        while (A[j] > pivot):
            j = j-1
        if (i < j):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[l]
    A[l] = A[j]
    A[j] = temp
    return j


main()
